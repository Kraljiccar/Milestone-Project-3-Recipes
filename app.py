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
    if category == "main":
        recipes = mongo.db.recipe.find({"category_name": "Main"})
    elif category == "appetizers":
        recipes = mongo.db.recipe.find({"category_name": "Appetizers"})
    elif category == "desserts":
        recipes = mongo.db.recipe.find({"category_name": "Dessert"})
    else:
        category == "all"
        recipes = mongo.db.recipe.find()
    return render_template ("recipes.html", recipes=recipes, page_title=category)

@app.route('/recipe/<recipe_id>')
def get_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("viewrecipe.html", recipe=recipe)


@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    return render_template("addrecipe.html", categories=categories, page_title="Add Recipe")

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return render_template("index.html")

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_recipe.html', recipe=recipe, page_title="Edit Recipe")

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update({"_id": ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name' :request.form.get('category_name'),
        'recipe_decription' :request.form.get('recipe_description'),
        'ingredients':request.form.get('ingredients'),
        'preparation_time':request.form.get('preparation_time'),
        'how_to':request.form.get('how_to'),
        'img_url':request.form.get('img_url')
    })
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)