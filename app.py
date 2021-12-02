from datetime import datetime

from flask import Flask, render_template, request, session, redirect, url_for, g
import database_mangement as db_manger
from register_user import registerUserForm
from login import login_form
from cryptography.fernet import Fernet

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


# page for drawing 
@app.route('/draw', methods=['GET', 'POST'])
def draw():
    if request.method == 'GET':
        return render_template('draw.html')
    if request.method == 'POST':
        # do nothing for now, in tutorial this is for saving the drawing as a file and inserting into a database
        # set this up to save to a database, but do not return a save file to the user for download
        return


if __name__ == '__main__':
    app.run('localhost', debug=True)
