from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, g, flash
from werkzeug.datastructures import MultiDict
from flask_wtf import csrf
from save_form import save_form
import database_mangement as db_manger
from confirmIdentity import confirmIdentity
from edit_profile_form import edit_profile_form
from register_user import registerUserForm
from login import login_form
from load_form import load_form
from werkzeug.security import generate_password_hash, check_password_hash
from flask_socketio import SocketIO
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'good_ol_secret_key'
# makes sure CSRF doesnt go out of context
csrf.CSRFProtect(app)
socketio = SocketIO(app)

# password hashing method
method = 'sha256'


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = db_manger.get_unique_user_by_id(session['user_id'])
        if len(user) > 0:
            g.user = user[0]


# main page of application
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    # create form
    form = registerUserForm()
    # if validation passes
    if form.validate_on_submit():
        # get data from form
        fn = form['first_name'].data
        ln = form['last_name'].data
        dob = form['dob'].data
        un = form['username'].data
        pw = generate_password_hash(form['password'].data, method=method)
        gd = form['gender'].data
        # insert into database
        db_manger.insert_user(un, pw, fn, ln, dob, gd)
        # go back home
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = login_form()
    if form.validate_on_submit():
        # remove current session
        session.pop('user_id', None)
        # get form data
        username = form['username'].data
        password = form['password'].data
        # retrieve user from database if exists
        user = db_manger.get_unique_user(username)
        # check if user exists and password matches
        if len(user) > 0 and check_password_hash(user[0][2], password):
            # set up session with user_id (id column in db)
            session['user_id'] = user[0][0]
            # redirect to profile page
            return redirect(url_for('profile'))
        # if no user, redirect back to login page
        flash("Username or Password invalid, please try again.")
        return redirect(url_for('login'))
    # if method is not post, go to login.hmtl
    return render_template('login.html', form=form)


@app.route('/signout')
def signout():
    # logs out of session, returns user back home
    session.pop('user_id', None)
    return redirect(url_for('home'))


@app.route('/profile')
def profile():
    # profile page shows details of user
    if not g.user:
        # if not logged in, redirect them to the login page
        return redirect(url_for('login'))
    return render_template('profile.html', g=g)


@app.route('/confirm_identity', methods=["GET", "POST"])
def confirm_identity():
    form = confirmIdentity()
    if form.validate_on_submit():
        password = form['password'].data
        if not check_password_hash(g.user[2], password):
            return redirect(url_for('confirm_identity'))
        return redirect(url_for('edit_profile'))
    return render_template('confirm_identity.html', g=g, form=form)


@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    # setting up default fields for user data
    if request.method == 'GET':
        form = edit_profile_form(
            formdata=MultiDict(
                {'first_name': g.user[4], 'last_name': g.user[5], 'dob': g.user[6], 'gender': g.user[7]}))
        return render_template("edit_profile.html", form=form)
    else:
        form = edit_profile_form(request.form)
        if form.validate_on_submit():
            new_pw = generate_password_hash(form['password'].data, method=method)
            fn = form['first_name'].data
            ln = form['last_name'].data
            dob = form['dob'].data
            gd = form['gender'].data
            # check for empty password string
            if check_password_hash(new_pw, ''):
                db_manger.update_user_by_id(g.user[0], g.user[2], fn, ln, dob, gd)
            else:
                db_manger.update_user_by_id(g.user[0], new_pw, fn, ln, dob, gd)
            return redirect(url_for('profile'))
        return render_template("edit_profile.html", form=form)


# page for drawing
@app.route('/draw', methods=['GET', 'POST'])
def draw():
    if request.method == 'GET':
        form = save_form()
        return render_template('draw.html', form=form)
    if request.method == 'POST':
        form = save_form(request.form)
        wbname = form['whiteboard_name'].data
        tdata = form['data'].data
        image = form['image'].data
        UUID = form['UUID'].data
        db_manger.insert_drawing(UUID, wbname, g.user[1], tdata, image)
        return redirect(url_for('home'))


@app.route('/load', methods=['GET', 'POST'])
def load():
    if g.user:
        if request.method == 'GET':
            form = load_form()
            data = db_manger.find_drawing_by_username(g.user[1])
            return render_template('load.html', form=form, user_wb=data)
        if request.method == 'POST':
            form = load_form(request.form)
            uuid = form['uuid'].data
            c_data = db_manger.find_drawing(uuid)
            if len(c_data) > 0:
                c_data = c_data
                form = save_form()
                return render_template('draw.html', form=form, data=c_data)
                # pass c_data to draw
            else:
                pass
                # put error message for data not found
            return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))


@app.route('/session')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    app.run('localhost', debug=True)
