# routes/app.py
from flask import Blueprint, render_template,  request, jsonify
from model.model import ask


Meal_app = Blueprint('Meal_app', __name__)

@Meal_app.route('/app')
def main():
    return render_template('app/index.html')

@Meal_app.route('/api/request', methods=['POST'])
def submit():
    try:
        # Extract ingredients and config from the request JSON
        data = request.get_json()
        ingredients = data.get('ingredients', [])
        
        # Default configuration for the API call
        default_config = {
            'model_name': 'gemini-1.5-flash'
        }
        
        # Override default config with any provided config only if the key exists in the default config
        user_config = data.get('config', {})
        config = {key: user_config.get(key, default_value) for key, default_value in default_config.items()}
        
        # Call the ask function to generate the meal plan
        meal_plan = ask(ingredients, config)
        
        # Return the generated meal plan as a JSON response
        return jsonify(meal_plan)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500