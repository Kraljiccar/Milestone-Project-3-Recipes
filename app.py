import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

if os.path.exists("env.py"):
    import env


app = Flask(__name__)



app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)



@app.route('/')
#displaying main page
@app.route('/recipes')
def index_recipe():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
   
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username':
                                        request.form.get('username').lower()})
        if existing_user is None:
            hash_password = bcrypt.hashpw(
                request.form['pasword'].encode('utf-8'), bcrypt.gensalt())
            users.insert_one({'username': request.form['username'],
                             'password': hash_password})
            session['username'] = request.form['username']
            return redirect(url_for('index_recipe'))
        
    return render_template('register.html', login_page=True)


@app.route('/login', methods=['POST', 'GET'])
def login():
   
    return render_template('login.html', login_page=True)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)