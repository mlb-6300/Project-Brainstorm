from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, g
import database_mangement as db_manger
from confirmIdentity import confirmIdentity
from register_user import registerUserForm
from login import login_form
from cryptography.fernet import Fernet

import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'good_ol_secret_key'

# fernet will be used to encrypt the password
# look up documentation, its pretty simple tbh
key = Fernet.generate_key()
f = Fernet(key)

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
        # pw = f.encrypt(str.encode(form['password'].data))
        pw = form['password'].data
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
        if len(user) > 0 and user[0][2] == password:
            # set up session with user_id (id column in db)
            session['user_id'] = user[0][0]
            # redirect to profile page
            return redirect(url_for('profile'))
        # if no user, redirect back to login page
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
        print(password)
        if g.user[2] != password:
            return redirect(url_for('confirm_identity'))
        return redirect(url_for('edit_profile'))
    return render_template('confirm_identity.html', g=g, form=form)


@app.route('/edit_profile')
def edit_profile():
    return render_template("edit_profile.html")


# page for drawing
@app.route('/draw', methods=['GET', 'POST'])
def draw():
    if request.method == 'GET':
        return render_template('draw.html')
    if request.method == 'POST':

        id = str(uuid.uuid4())
        wbname = request.form['wb_name']
        data = request.form['save_cdata']
        canvas_image = request.form['save_image']

        #db_manger.insert_drawing(id, wbname, user, data, canvas_image)

        return redirect(url_for('index'))


@app.route('/load', methods=['GET', 'POST'])
def load():
    return


# @app.route('/save', methods=['GET','POST'])
# def save():


if __name__ == '__main__':
    app.run('localhost', debug=True)

# (id, WBName, Username, Timestamp, data, canvas_image)
