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

@app.route('/recipes/<category>')
def get_all(category):
    if category == "all":
        category = "All recipes"
        recipe = mongo.db.recipe.find() 
    else:
        recipe = mongo.db.recipe.find({"$text": {"$search": category}})
    return render_template("recipes.html", recipe=recipe, page_title=category)
    
@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('viewrecipe.html')
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)