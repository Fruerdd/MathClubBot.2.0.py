import sqlite3
connection = sqlite3.connect('tgUsers.db')
cursor = connection.cursor()


def start_table():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
    tg_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    last_date DATETIME,
    last_step TEXT NOT NULL
    )
    """)
    connection.commit()


def info_table(tg_id, username):
    data = cursor.execute("SELECT 1 FROM Users WHERE tg_id == '{key}'".format(key=tg_id)).fetchone()
    if not data:
        cursor.execute("INSERT INTO Users VALUES (?,?,?,?)", (tg_id, username, '', ''))
        connection.commit()


def update_last_step(tg_id, date, section):
    cursor.execute('UPDATE Users SET last_step = ? WHERE tg_id = ?', (section, tg_id))
    cursor.execute('UPDATE Users SET last_date = ? WHERE tg_id = ?', (date, tg_id))
    connection.commit()


def labels_create():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS User_labels (
    tg_id 
        INTEGER 
            PRIMARY KEY
    ,labels 
        TEXT
    )
    """)
    connection.commit()


def labels_edit(tg_id, all_labels):
    cursor.execute('UPDATE User_labels SET labels = ? WHERE tg_id = ?', (all_labels, tg_id))
    connection.commit()





