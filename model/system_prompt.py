


def build_system_prompt(ingredients):
    """
    Builds a system prompt for the Gemini API based on user ingredients.
    
    Args:
        ingredients (list): List of ingredients user has.
    
    Returns:
        str: The prompt string for the AI model.
    """
    
    prompt = (
        "You are a helpful AI that creates meal plans based on available ingredients. "
        "Here is a list of ingredients the user has: "
        f"{', '.join(ingredients)}. "
        "Please generate a meal plan in the following JSON format: "
        """
        {
            "meal_plan": {
                "breakfast": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    }
                },
                "lunch": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    }
                },
                "dinner": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    }
                },
                "snacks": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    }
                }
            }
        }
        """
        "Make sure the response is in valid JSON. The recipe steps should be clear and concise."
    )

    
    return prompt
