from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, g
import json
from functools import wraps
from werkzeug import secure_filename
import os







# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'nexisadmin'
PASSWORD = 'changeme'

UPLOAD_FOLDER = 'images/'
ALLOWED_EXTENSIONS = set(['jpg', 'png','jpeg','gif'])
 


app = Flask(__name__)
app.config.from_object(__name__)

app.crew_members = []

@app.before_first_request
def init():
    print "I AM INIT"
    f = open('data/crew_members.json', 'r')
    raw_data = f.read()
    json_data = json.loads(raw_data)
    app.crew_members = json_data
    print app.crew_members
    #load users data file

def save_user(user):
    #TODO ERROR HANDLING
    for i in xrange(len(app.crew_members)):
        if app.crew_members[i]['name'] == user['name']:
            app.crew_members[i] = user
            print app.crew_members[i]
            update_file()
            return
    app.crew_members.append(user)
    update_file()
    return

def update_file():
    #TODO ERROR HANDLING
    f =  open('data/crew_members.json', 'w')
    jsondatas = json.dumps(g.get('crew_members'))
    f.write(jsondatas)
    f.close()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS



@app.route('/')
def index():
    return "Welcome to the night's watch!"





@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if session.get('logged_in') == True:
         return redirect(url_for('nightswatch'))
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('nightswatch'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

def login_required(f):
     @wraps(f)
     def decorated_function(*args, **kwargs):
         if session.get('logged_in') is None or session.get('logged_in') == False:
             return redirect(url_for('login', next=request.url))
         return f(*args, **kwargs)
     return decorated_function

@app.route('/nightswatch')
@login_required
def nightswatch():
    return json.dumps(app.crew_members)

@app.route('/nightswatch/new', methods=['GET', 'POST'])
@login_required
def new():
    error = None
    if request.method == 'POST':
        print "POST"
        name = request.form.get('name',None)
        major = request.form.get('major',None)
        twitter = request.form.get('twitter',None)
        linkedin = request.form.get('linkedin',None)
        github = request.form.get('github',None)
        bio = request.form.get('bio',None)
        filename = None

        file = request.files.get('image')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print (os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        newuser = {'name':name, 'major': major, 'twitter': twitter, 'linkedin':linkedin,'github':github, 'bio':bio, 
        'filename':filename}
        save_user(newuser)

        #store data and return redirector
        return "SAVING DATAS"

    return render_template('new.html', error=error)


if __name__=='__main__':
    app.debug = True
    app.run()



