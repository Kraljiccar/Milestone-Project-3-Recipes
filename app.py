import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'Recipe'
app.config["MONGO_URI"] = 'mongodb+srv://root1:r00tUser@myfirstcluster.of3gn.mongodb.net/<recipe>?retryWrites=true&w=majority'



@app.route('/')
#displaying main page
@app.route('/recipes')
def index_recipe():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)