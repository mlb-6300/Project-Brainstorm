# creates database and tables for user data and saved whiteboards

import sqlite3

conn = sqlite3.connect('userData.db')

# creating the User table
conn.execute(
    """
            CREATE TABLE IF NOT EXISTS Users(
                id       INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT UNIQUE NOT NULL,
                Password TEXT NOT NULL,
                Created DATETIME NOT NULL,
                First_Name TEXT NOT NULL,
                Last_Name TEXT NOT NULL,
                DOB DATE NOT NULL,
                Gender TEXT NOT NULL
            )
    """
)

# creating the Whiteboards table
conn.execute(
    """
            CREATE TABLE IF NOT EXISTS Whiteboards(
                id     text,
                WBName TEXT NOT NULL,
                Username TEXT NOT NULL,
                Timestamp DATETIME NOT NULL,
                data TEXT NOT NULL,
                canvas_image TEXT NOT NULL, 
                PRIMARY KEY (id),
                FOREIGN KEY (Username) REFERENCES Users(Username)
            )
    """
)
