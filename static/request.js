document.getElementById("mealForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const ingredients = document
        .getElementById("ingredients")
        .value.split(",")
        .map((item) => item.trim());

    try {
        const response = await fetch("http://127.0.0.1:5000/api/request", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                ingredients: ingredients,
                config: {
                    model_name: "gemini-1.5-flash-latest",
                },
            }),
        });

        const data = await response.json();

        displayMealPlan(data);
    } catch (error) {
        console.error("Error:", error);
    }
});

function displayMealPlan(data) {
    const mealPlanResults = document.getElementById("mealPlanResults");
    mealPlanResults.innerHTML = "";

    let { meal_plan } = data[0];


    Object.keys(meal_plan).forEach((key) => {
        const mealType = meal_plan[key];
        
        const mealName = document.createElement("h2");
        mealName.textContent = `${key.charAt(0).toUpperCase() + key.slice(1)}: ${mealType.name}`;

        const recipeSteps = document.createElement("ul");
        mealType.recipe.steps.forEach((step) => {
            const listItem = document.createElement("li");
            listItem.textContent = step;
            recipeSteps.appendChild(listItem);
        });

        mealPlanResults.appendChild(mealName);
        mealPlanResults.appendChild(recipeSteps);
    });
}
