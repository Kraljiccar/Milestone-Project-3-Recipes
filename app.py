import os

from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
from os import path
if path.exists("env.py"):
  import env 
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Recipe'
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")




@app.route('/')
#displaying main page
@app.route('/recipes')
def index_recipe():
    return render_template('index.html')

@app.route('/register')
def register():
    
    if 'username' in session:
        return redirect(url_for('index'))

    form = RegisterForm()
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                     bcrypt.gensalt())
# generate password hash
            users.insert({'name': request.form['username'],
                          'password': hashpass})
            session['username'] = request.form['username']
            # User is now successfully logged in
            session['username'] = request.form['username']
            flash('User creation successful!')
            return redirect(url_for('index'))

        flash('That username already exists!')

    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)