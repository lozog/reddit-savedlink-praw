from flask import Flask
import sqlite3

app = Flask(__name__)
app.config.from_object('config')

from src import controller, models
