from src import app

import praw
import sqlite3

from flask import render_template

from reddit_savedlink import *
from db_create import *

nothumb = 'nothumb'
DB_PATH = 'savedlinks.db'

@app.route('/')
@app.route('/index')
def index():
    print 'index'
    # creates DB if necessary
    db_create(DB_PATH)

    # fetches from DB
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    savedLinksResult = cursor.execute("SELECT * FROM savedlinks")

    savedLinks = savedLinksResult.fetchall()

    # for row in savedLinks:
        # print "row: %s" % row

    print "done"
    cursor.close()
    connection.close()

    theUser = {'name': 'tom---swift'}

    return render_template('index.html',
                           theUser=theUser,
                           savedLinks=savedLinks,
                           nothumb=nothumb)

@app.route('/getSavedLinks', methods=['POST'])
def getSavedLinksFromReddit():
    # clear db first
    db_delete(DB_PATH)

    savedLinks = getSavedLinks('list',100,0)
    # savedLinks = getSavedLinks('list',1,1)

    connection = sqlite3.connect('savedlinks.db')
    cursor = connection.cursor()

    print "%d savedLinks to process" % len(savedLinks)
    for savedLink in savedLinks:
        # pull data out of json
        fullname     = savedLink['name']
        kind         = fullname[:2]
        title        = savedLink['link_title'] if (kind == 't1') else savedLink['title']
        url          = savedLink['link_url']   if (kind == 't1') else savedLink['url']
        if kind == 't3':
            if 'preview' in savedLink:
                thumbnail = savedLink['preview']['images'][0]['source']['url']
            else:
                # possible values: self, default
                thumbnail = savedLink['thumbnail']
        else:
            thumbnail = 'nothumb'
        print thumbnail
        subreddit    = savedLink['subreddit'].display_name
        subreddit_id = savedLink['subreddit_id']

        # if 'preview' in savedLink:
        #     print savedLink['preview']['images'][0]['source']['url']
        # print thumbnail

        # print savedLink['preview']['images'][0]['source']['url']
        # for item in savedLink['preview']['images']:
        #     print item
        #     print '\n'
        # print "done"
        # print("%s: %s - %s" % (fullname, title, url))

        # insert into DB
        if True:
            sql = "INSERT INTO savedlinks VALUES (?, ?, ?, ?, ?, ?, ?)"
            args = fullname, kind, title, url, thumbnail, subreddit, subreddit_id
            cursor.execute(sql, args)

    cursor.close()
    connection.commit()
    connection.close()

    print 'got SavedLinks'

    return render_template('mainlisting-card.html',
                            savedLinks=savedLinks,
                            nothumb=nothumb)
