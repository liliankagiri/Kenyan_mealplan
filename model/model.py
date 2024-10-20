import google.generativeai as genai
from datetime import datetime
import os
import json

# Correcting imports with proper relative paths
from .system_prompt import build_system_prompt, MealPlan
from .config import configure_api

# Initialize the API
api_key = configure_api()

if api_key is None:
    raise RuntimeError("API Key not configured correctly")

genai.configure(api_key=api_key)

def ask(ingredients, config):
    """
    Sends a request to the Gemini API and saves the response to a .txt file.
    
    Args:
        ingredients (list): List of ingredients user has.
        config (dict): Configuration options.
        
    Returns:
        dict: The AI response as a dictionary or an error code.
    """

    try:
        # Build the system prompt
        prompt = build_system_prompt(ingredients)
        
        # Use the API model with JSON response MIME type
        model_name = config.get('model_name', 'gemini-1.5-flash-latest')
        model = genai.GenerativeModel(model_name, generation_config={"response_mime_type": "application/json"})
        response = model.generate_content(prompt, generation_config=genai.GenerationConfig(
        response_mime_type="application/json", response_schema=list[MealPlan]
    ),
)
        
        # Ensure the response directory exists
        response_dir = os.path.join(os.path.dirname(__file__), "response")
        if not os.path.exists(response_dir):
            os.makedirs(response_dir)
        
        # Save the response in a timestamped .json file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_path = os.path.join(response_dir, f"response_{timestamp}.json")
        with open(file_path, 'w') as file:
            file.write(response.text)
        
        # Since the response is expected in JSON format, we return it directly as a dictionary
        return json.loads(response.text)
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return {"error": str(e)}
