from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import sqlite3



app = Flask(__name__)
app.config.from_object('config')

# db = SQLAlchemy(app)

from src import controller, models
