from flask import Flask
from flask import render_template

from reddit_savedlink import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    savedLinks = getSavedLinks("list")

    theUser = {'name': 'tom---swift'}

    return render_template('mainlisting.html',
                           theUser=theUser,
                           savedLinks=savedLinks)

if __name__ == "__main__":
    app.run()
