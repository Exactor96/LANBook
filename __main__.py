import os

from flask import Flask,request, render_template
from forms import NoteForm
import sqlite3

DB_NAME='db.sqlite3'
db_connect = sqlite3.connect(DB_NAME)
db_connect.execute("""CREATE TABLE IF NOT EXISTS 'Notes' (
  'id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
  'title' varchar(255) NOT NULL,
  'text' TEXT ,
  'file' BLOB);""")

app = Flask(__name__,template_folder='templates')
cur = db_connect.cursor()
@app.route('/add',methods=['post','get'])
def add_note():
    note_form = NoteForm()

    if note_form.validate_on_submit():
        title = note_form.title.data
        text = note_form.text.data
        file = note_form.file.data
        with sqlite3.connect(DB_NAME) as con:
            cur = con.cursor()
            cur.execute(f'''insert into Notes(title,text) values('{title}','{text}')''')
            con.commit()
    return render_template('add.html',form=note_form)
@app.route('/')
def index():
    with sqlite3.connect(DB_NAME) as con:
        cur = con.cursor()
        notes=cur.execute('select * from Notes').fetchall()
        return render_template('index.html',note_list=notes)

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=False)
