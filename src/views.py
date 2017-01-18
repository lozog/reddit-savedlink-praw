from src import app, db, models

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from reddit_savedlink import *

# this is also the controller

@app.route("/")
@app.route("/index")
def index():
    # savedLinks = getSavedLinks("list")

    # u = models.SavedLink(fullname='test', title='test title', url='www.google.com')
    # db.session.add(u)
    # db.session.commit()
    savedLinks = models.SavedLink.query.all()

    theUser = {'name': 'tom---swift'}

    return render_template('index.html',
                           theUser=theUser,
                           savedLinks=savedLinks)

@app.route("/getSavedLinks", methods=['POST'])
def getSavedLinksFromReddit():
    savedLinks = getSavedLinks("list")
    # savedLinks = models.SavedLink.query.all()

    print "getSavedLinks"
    # TODO: store saved links in db
    return render_template('mainlisting.html',
                            savedLinks=savedLinks)
