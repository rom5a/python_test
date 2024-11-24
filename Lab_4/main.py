import re
from typing import List

input_date = ['2 eggs', '200 grams of flour', '150 gram of suger']
persons = 3
def adjust_quantities(nm_persons: int, ingredients: List[str]) -> List[str]:
    modified_ingredients =[]
    for ingredient in ingredients:
        numbers = re.findall(r'\d+',ingredient)
        modified_number = int(numbers[0]) * nm_persons
        modified_ingredient = ingredient.replace(numbers[0],str(modified_number))
        modified_ingredients.append(modified_ingredient)

    return modified_ingredients


print(adjust_quantities(persons, input_date))
