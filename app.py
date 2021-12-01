from datetime import datetime

from flask import Flask, render_template, request
import database_mangement as db_manger
from register_user import registerUserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'good_ol_secret_key'





# import cryptography.fernet


# fernet will be used to encrypt the password
# look up documentation, its pretty simple tbh
# key = cryptography.fernet.Fernet.generate_key()
# f = cryptography.fernet.Fernet(key)

# main page of application
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = registerUserForm()
    if form.validate_on_submit():
        fn = form['first_name'].data
        ln = form['last_name'].data
        dob = form['dob'].data
        un = form['username'].data
        pw = form['password'].data
        gd = form['gender'].data
        db_manger.insert_user(un, pw, fn, ln, dob, gd)
        return render_template('index.html')
    return render_template('register.html', form=form)


@app.route('/login')
def login():
    return render_template('login.html')


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
