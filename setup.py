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

                PRIMARY KEY (Username)
            )
    """
)

conn.execute(
    """
            CREATE TABLE Whiteboards(
                WBName VARCHAR(40),
                Username VARCHAR(40),
                Timestamp DATETIME
            )
    """
)