from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
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
  
# def insert_message(request):
#         msg = request.form['message']
#         handle = request.form['handle']

#         with get_message_db() as db:
#                 cursor = db.cursor()

#                 cursor.execute("SELECT COUNT(*) FROM messages")
#                 id = cursor.fetchone()[0] + 1

#                 cmd = \
#                 f"""
#                 INSERT INTO messages(id, handle, message)
#                 VALUES({id}, '{handle}', '{msg}')
#                 """

#                 cursor.execute(cmd)
#                 db.commit()

#         return [msg, handle]

# def render_submit():
#         if request.method == "GET":
#                return render_template("submit.html")
#         else:
#                message, handle = insert_message()
#                return render_template("submit.html",
#                                       message,
#                                       handle,
#                                       thanks = True)

# @app.route("/view/")    
# def random_messages(n):
#         with get_message_db() as db:
#                 cursor = db.cursor()

#                 cmd = \
#                 f"""
#                 SELECT message, handle
#                 FROM messages
#                 ORDER BY RANDOM()
#                 LIMIT {n}
#                 """

#                 cursor.execute(cmd)
#                 # returns a list of tuples with message and handle
#                 result = [cursor.fetchone() for i in range(n)]
#                 g.message_db.close()

#         return result

# def render_view():
#        MsgHandleList = random_messages(5)
#        return render_template("view.html")