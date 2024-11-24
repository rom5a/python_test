import re
from typing import List

persons = 3


def adjust_quantities(nm_persons: int, ingredients: List[str]) -> List[str]:
    modified_ingredients =[]
    for ingredient in ingredients:
        numbers = re.findall(r'\d+',ingredient)
        modified_number = int(numbers[0]) * nm_persons
        modified_ingredient = ingredient.replace(numbers[0],str(modified_number))
        modified_ingredients.append(modified_ingredient)

    return modified_ingredients

def open_file(file_name):
    array = []
    with open(file_name) as f:
        for line in f:
            array.append(line)
    return array

data = open_file('data.txt')

print (adjust_quantities(persons, data))