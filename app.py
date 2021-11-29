from flask import Flask, render_template, request
import sqlite3 as sql
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/draw', methods=['GET', 'POST'])
def draw():
    if request.method == 'GET':
        return render_template('draw.html')
    if request.method == 'POST':
        # do nothing for now, in tutorial this is for saving the drawing as a file and inserting into a database
        # set this up to save to a database, but do not return a save filed to the yesterday for download
        return 



if __name__ == '__main__':
    app.run('localhost', debug=True)