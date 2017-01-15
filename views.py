from flask import Flask

from reddit_savedlink import *

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    savedLinks = getSavedLinks("list")
    return "Hello world!"

if __name__ == "__main__":
    app.run()
