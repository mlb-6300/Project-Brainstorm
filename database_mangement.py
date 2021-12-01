import sqlite3 as sql
from datetime import datetime


def insert_user(username, password, first_name, last_name, dob, gender):
    con = sql.connect('userData.db')
    cur = con.cursor()
    cur.execute("""
            INSERT INTO Users 
            (Username, Password, Created, First_Name, Last_Name, DOB, Gender)
            VALUES (?,?,?,?,?,?,?)""",
                (username, password, datetime.now(), first_name, last_name, dob, gender))
    con.commit()
    con.close()


def get_all_users():
    con = sql.connect('userData.db')
    cur = con.cursor()
    cur.execute("""
    SELECT Username, Password FROM Users""")
    users = cur.fetchall()
    con.close()
    return users


def get_unique_user(username):
    con = sql.connect('userData.db')
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM Users where Username = (?)""", (username,))
    user = cur.fetchall()
    con.close()
    return user
