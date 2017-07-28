import sqlite3
import os

def db_create(path):
    print(path)
    print(os.getcwd())
    if os.path.exists(path):
        print("returning")
        return

    print("creating db")

    # connect to db
    conn = sqlite3.connect(path)
    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE savedlinks
                 (
                 fullname       text,
                 kind           text,
                 title          text,
                 url            text,
                 thumbnail      text,
                 subreddit      text,
                 subreddit_id   text
                 )''')

def db_delete(path):
    if not os.path.isfile(path):
        return

    os.remove(path)
    db_create(path)
