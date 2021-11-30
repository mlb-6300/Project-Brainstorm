import sqlite3

conn = sqlite3.connect('userData.db')

conn.execute(
    """
            CREATE TABLE IF NOT EXISTS Users(
                Username VARCHAR(40) PRIMARY KEY,
                Password VARCHAR(40),
                Created DATETIME,
                First_Name VARCHAR(30),
                Last_Name VARCHAR (30),
                DOB DATE,
                Gender CHAR(1)
            )
    """
)

conn.execute(
    """
            CREATE TABLE IF NOT EXISTS Whiteboards(
                WBName VARCHAR(40),
                Username VARCHAR(40),
                Timestamp DATETIME
            )
    """
)
