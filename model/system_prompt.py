import enum
from typing import List, Optional, TypedDict

class MealType(enum.Enum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACKS = "snacks"

class RecipeSteps(TypedDict):
    steps: List[str]

class Recipe(TypedDict):
    name: str
    ingredients: List[str]
    recipe: RecipeSteps
    cooking_time: Optional[int]
    health_score: Optional[int]

class MealPlanDetails(TypedDict):
    breakfast: Recipe
    lunch: Recipe
    dinner: Recipe
    snacks: Recipe

class MealPlan(TypedDict):
    meal_plan: MealPlanDetails

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
                    },
                    "cooking_time": int,  
                    "health_score": int  
                },
                "lunch": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    },
                    "cooking_time": int,  
                    "health_score": int  
                },
                "dinner": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    },
                    "cooking_time": int,  
                    "health_score": int  
                },
                "snacks": {
                    "name": "string",
                    "ingredients": ["string", ...],
                    "recipe": {
                        "steps": ["string", ...]
                    },
                    "cooking_time": int,  
                    "health_score": int  
                }
            }
        }

        cooking_time and health_score should be integers.
        cooking_time is in minutes.
        health_score is a number from 1 to 10, where 10 is the healthiest.
        """
        "Make sure the response is in valid JSON. The recipe steps should be clear and concise."
    )

    return prompt