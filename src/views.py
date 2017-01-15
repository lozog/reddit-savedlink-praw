from src import app

from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from reddit_savedlink import *

@app.route("/")
@app.route("/index")
def index():
    savedLinks = getSavedLinks("list")

    theUser = {'name': 'tom---swift'}

    return render_template('mainlisting.html',
                           theUser=theUser,
                           savedLinks=savedLinks)
