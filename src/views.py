from src import app, db, models

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from reddit_savedlink import *

@app.route("/")
@app.route("/index")
def index():
    # savedLinks = getSavedLinks("list")

    # u = models.SavedLink(fullname='test', title='test title', url='www.google.com')
    # db.session.add(u)
    # db.session.commit()
    savedLinks = models.SavedLink.query.all()

    theUser = {'name': 'tom---swift'}

    return render_template('mainlisting.html',
                           theUser=theUser,
                           savedLinks=savedLinks)
