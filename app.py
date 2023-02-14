from flask import Flask
from flask import render_template, abort, redirect, url_for
from flask import request
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def get_message_db():
  # write some helpful comments here
  try:
          return g.message_db
  except:
          g.message_db = sqlite3.connect("messages_db.sqlite")
          cmd = '' # replace this with your SQL query
          cursor = g.message_db.cursor()
          cursor.execute(cmd)
          return g.message_db