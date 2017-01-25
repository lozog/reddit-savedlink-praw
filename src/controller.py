from src import app, db, models

import praw

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from reddit_savedlink import *

from user import user,pw

@app.route('/')
@app.route('/index')
def index():

    # fetches from DB
    savedLinks = models.SavedLink.query.all()
    # savedLinks = []

    theUser = {'name': 'tom---swift'}

    return render_template('index.html',
                           theUser=theUser,
                           savedLinks=savedLinks)

@app.route('/getSavedLinks', methods=['POST'])
def getSavedLinksFromReddit():
    savedLinks = getSavedLinks('list',100,0)
    # savedLinks = models.SavedLink.query.all()
    print len(savedLinks)
    for savedLink in savedLinks:
        # pull data out of json

        fullname     = savedLink['name']
        kind         = fullname[:2]
        title        = savedLink['link_title'] if (kind == 't1') else savedLink['title']
        url          = savedLink['link_url']   if (kind == 't1') else savedLink['url']
        thumbnail    = savedLink['thumbnail']  if (kind == 't3') else 'nothumb'
        subreddit    = savedLink['subreddit'].display_name
        subreddit_id = savedLink['subreddit_id']

        print('%s: %s - %s' % (fullname, title, url))


        # create model, insert into DB
        if False:
            u = models.SavedLink(fullname     = fullname,
                                 kind         = kind,
                                 title        = title,
                                 url          = url,
                                 thumbnail    = thumbnail,
                                 subreddit    = subreddit,
                                 subreddit_id = subreddit_id )
            db.session.add(u)
            db.session.commit()

    print 'getSavedLinks'
    # TODO: store saved links in db
    return render_template('mainlisting.html',
                            savedLinks=savedLinks)
