from src import app, db, models

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from reddit_savedlink import *

# this is also the controller

@app.route("/")
@app.route("/index")
def index():
    # savedLinks = getSavedLinks("list")

    savedLinks = models.SavedLink.query.all()
    # savedLinks = []

    theUser = {'name': 'tom---swift'}

    return render_template('index.html',
                           theUser=theUser,
                           savedLinks=savedLinks)

@app.route("/getSavedLinks", methods=['POST'])
def getSavedLinksFromReddit():
    savedLinks = getSavedLinks("list",15,1)
    # savedLinks = models.SavedLink.query.all()
    print len(savedLinks)
    for savedLink in savedLinks:
        # pull data out of json



        fullname = savedLink["name"]
        kind     = fullname[:2]
        title    = savedLink["link_title"] if (kind == "t1") else savedLink["title"]
        url      = savedLink["link_url"] if (kind == "t1") else savedLink["url"]

        print('%s: %s - %s' % (fullname, title, url))


        # create model, insert into DB
        # u = models.SavedLink(fullname='test', title='test title', url='www.google.com')
        # db.session.add(u)
        # db.session.commit()

    print "getSavedLinks"
    # TODO: store saved links in db
    return render_template('mainlisting.html',
                            savedLinks=savedLinks)
