from model.model import ask

def main():
    # Example list of ingredients
    ingredients = ["beef", "potatoes", "broccoli", "cheese", "pasta"]
    
    # Configuration for the API call
    config = {
        'model_name': 'gemini-1.5-flash'
    }
    
    # Ask the AI for a meal plan
    response = ask(ingredients, config)
    
    print("Generated Meal Plan:", response)

if __name__ == "__main__":
    main()
