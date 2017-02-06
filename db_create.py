import sqlite3

# connect to db
conn = sqlite3.connect('savedlinks.db')
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
