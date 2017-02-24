from flask import Flask
import sqlite3

app = Flask(__name__)

from src import controller
