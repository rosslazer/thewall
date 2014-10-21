from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from functools import wraps
import sqlite3




data = ""
user = {'userid':'23423432', 'username': 'nexisadmin', 'password': 'changeme'}


# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = user['username']
PASSWORD = user['password']



app = Flask(__name__)
app.config.from_object(__name__)
#def init():
    #load user auth file
    #load users data file
   #return "DSFDS"

@app.route('/')
def index():
    return "Welcome to the night's watch!"





@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for('login', next=request.url))
#         return f(*args, **kwargs)
#     return decorated_function




if __name__=='__main__':
    app.debug = True
    app.run()


