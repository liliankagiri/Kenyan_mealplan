# app.py
from flask import Flask
from routes.home import home
from routes.app import Meal_app



app = Flask(__name__)

# Register the blueprint
app.register_blueprint(home)
app.register_blueprint(Meal_app)

if __name__ == '__main__':
    app.run(debug=True)
