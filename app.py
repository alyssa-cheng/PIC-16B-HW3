from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

def get_message_db():
  # write some helpful comments here
  try:
        return g.message_db
  except:
        g.message_db = sqlite3.connect('messages_db.sqlite')
        
        cmd = \
        """
        CREATE TABLE IF NOT EXISTS messages
        (id INTEGER, handle TEXT, message TEXT)
        """

        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db
  
def insert_message(request):
        message = request.form['message']
        handle = request.form['handle']

        with get_message_db() as db:
                cursor = db.cursor()

                cursor.execute("SELECT COUNT(*) FROM messages")
                id = cursor.fetchone()[0] + 1

                cmd = \
                f"""
                INSERT INTO messages(id, handle, message)
                VALUES({id}, '{handle}', '{message}')
                """

                cursor.execute(cmd)
                db.commit()

        return [message, handle]

def random_messages(n):
        with get_message_db() as db:
                cursor = db.cursor()

                cmd = \
                f"""
                SELECT message, handle
                FROM messages
                ORDER BY RANDOM()
                LIMIT {n}
                """

                cursor.execute(cmd)
                # returns a list of tuples with message and handle
                result = cursor.fetchall()

        return result

@app.route("/", methods = ["GET", "POST"])
def render_submit():
        if request.method == "GET":
               return render_template("submit.html")
        else:
               insert_message(request)
               return render_template("submit.html", thanks = True)

@app.route("/view/")    
def render_view():
       MsgHandleList = random_messages(5)
       return render_template("view.html", MsgList = MsgHandleList)