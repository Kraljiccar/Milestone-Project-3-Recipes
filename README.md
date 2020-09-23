## Data Centric Development Milestone Project 
# Serbian Kitchen

Serbian kitchen is online cookbook where users can browse, add, edit or delete recipes. Clean and simple, recipes are menages by 3 categories, appetizers, main food and desserts.

<img src="https://github.com/Kraljiccar/Milestone-Project-3-Recipes/blob/master/static/imgs/sk.png?raw=true" margin="0">

[Deployed link here](https://milestone-project-3-recipes.herokuapp.com/)

## UI/UX

### Project goals
Serbian Kitchen is milestone project for Code Institute Data Centric Development module. The goal of this project is to create, store, edit and delete recipes (CRUD).
Target audience for this project is people that are simply interested in Serbian/Balkan cooking. My goal was to create online cookbook without any unnecesarry long
descriptions - only straight-to-the-point recipes.

### Developer goals
* Provide a simple, easy to use online cookbook where user can browse, post, edit and delete recipes, filter them by categories.
* By practice Python and non-relational database MongoDb.
* Improve Bootstrap knowledge.
* Learn to use Heroku Pages

### Design

Main inspiration for Serbian Kitchen is my origin, because i miss that original food, since i live i Sweden, where the food is not so tasty.

I chose to override all B4 round corners on images, forms and buttons to suit my design. I choose white background color because the colors of recipe images are very colorfull and all over the spectrum.

To build the design of the page I used Bootstrap 4, FontAwesome.

Actualy i haven't done much browsing, made a site totally out of my head to be ass simple ass posible. After a googleing, i have realised that there is no Serbian Kitchen website. 

During development i tried to simplified site ass much ass possible. 

### Wireframes 

<img src="https://github.com/Kraljiccar/Milestone-Project-3-Recipes/blob/master/static/imgs/allrecipes.png?raw=true" margin="0">

## Features

### Existing features
* Sorting by category by clicking navigation links.
* Index page contains pleasent photos sorted in carousel.
* Social icons with links in the page footer
* Bootstrap input field validation
* Recipes displayed in list have title, description, cooking time and user information
* Create, read, update, delete recipe (CRUD)
* Carousel

### Future features
* Search: users are able to search for recipes by username, title or any other text. If no results are found message "No results found. Please try again".
* Sign Up
* Login
* Google login
* "Remember me" signup checkbox
* Recipe image url validation
* More categories
* Admin console
* Admin able to add/edit/delete categories
* Recipe Comments

### Information Architecture
MongoDB Atlas is used for storing data for this web site.

| categories            | recipe        | 
| --------------------- |:-------------:|
| category_name: string | recipe_name: string |
|                       | category_name: string |
|                       | recipe_description : string |
|                       | ingredients: string |
|                       | preparation_time: string |
|                       | how_to: string |
|                       | img_url: string |

For the needs of this website I did not find the need to use other data types in MongoDB. In a real world application I would add image file uploads, dynamic input fields and rich text editing.

### Technologies used
* HTML5
* CSS3
* jQuery
* Python 3.8.2 (flask)
* MongoDB
* Bootstrap CDN
* Git & GitHub.com
* Heroku.com pages
* FontAwesome.com
* Google Fonts
* Google Chrome Developer tools

### Manuel Testing  
I extensively tested the page on laptop, mobile and iPad Pro 13" tablet after every major development test. 

### Heroku
Heroku was chosen as the deployment platform for this project. The steps to deploy the local app to Heroku were as follow:
In Heroku, create an app. The app must have a unique name.
Link that app to the GitHub repository by going to the "Deploy" tab in the main app menu.
In the Settings tab, add the corresponding Config Variables as present in local development:
1. MONGO_URI mongodb+srv://...
2. IP 0.0.0.0
3. PORT 5000
4. SECRET_KEY
Created "Procfile" by typing:
5. $ echo web: python app.py > Procfile
Push repo to Heroku
6. $ git push heroku master

## Credits
### Code
* Code Intitute
### Images
* [Pixabay] (https://pixabay.com/sv/)
### Content
* Recipes taken from various websites.
