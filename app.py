from datetime import datetime

from flask import Flask, render_template, request
from datetime import datetime
import sqlite3 as sql

from cryptography.fernet import Fernet

app = Flask(__name__)

# fernet will be used to encrypt the password
# look up documentation, its pretty simple tbh
key = Fernet.generate_key()
f = Fernet(key)

# main page of application
@app.route('/')
def home():
    return render_template('index.html')
  
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/doRegistration', methods=['POST', 'GET'])
def doRegistration():
    if request.method == 'POST':
        try:
            fn = request.form['firstName']
            ln = request.form['lastName']
            dob = request.form['DOB']
            un = request.form['userName']
            pw = request.form['password']
            gd = request.form['gender']

            with sql.connect("userData.db") as con:
                cur = con.cursor()

                cur.execute("""
                INSERT INTO Users 
                (Username, Password, Created, First_Name, Last_Name, DOB, Gender)
                VALUES (?,?,?,?,?,?,?)""", (un, pw, datetime.now(), fn, ln, dob, gd))

        except Exception as e:
            print(e)
        finally:
            return home()


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
