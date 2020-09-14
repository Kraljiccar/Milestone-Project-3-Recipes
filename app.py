import os
from flask import (
    Flask, flash, render_template,
    redirect, request, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__) 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app) 
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recipes/')
def recipes():
    return render_template("recipes.html", recipes=mongo.db.recipe.find())



@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    return render_template("addrecipe.html", categories=categories, page_title="Add Recipe")

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return render_template(url_for('recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)