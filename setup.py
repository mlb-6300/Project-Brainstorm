import sqlite3

conn = sqlite3.connect('userData.db')

conn.execute(
    """
            CREATE TABLE Users(
                Username VARCHAR(40),
                Password VARCHAR(40),
                Created DATETIME,
                DOB DATE,
                Gender CHAR(1)
            )
    """
)