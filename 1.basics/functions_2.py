# Return values
# An argument optional - put an empty string as a default and place at the end of the list of parameters
def formatted_full_name(first_name, last_name, middle_name=''):
    """Return a full name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

actress = formatted_full_name('lily', 'thomson', 'chloe ninette')
print(actress)

actor = formatted_full_name('brad', 'pitt')
print(actor)

# Preventing a function from modifying a list - using [:] with the argument list
def recipe(ingredients, curry):
    """
    Get a ingredients for the food
    """
    while ingredients:
        ingredient = ingredients.pop()
        print("Essential ingredient: " + ingredient)
        curry.append(ingredient)

ingredients = ['onion', 'garlic', 'salt', 'pepper', 'carrot', 'chili', 'potato']
curry = []
recipe(ingredients[:], curry)
print("\nCurry's essential ingredients: ")
print(curry)

