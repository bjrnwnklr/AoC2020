from collections import defaultdict

# f_name = 'ex1.txt'
f_name = 'input.txt'

all_ingredients = set()
possible_allergens = dict()
recipes = list()

with open(f_name, 'r') as f:
    for i, line in enumerate(f.readlines()):
        # get a list of the ingredients and record the food recipe as a set of the
        # ingredients (recipes = [{'aaa', 'bbb'}, {...}]
        ingredients = line.split(' (')[0].strip().split()
        recipes.append(set(ingredients))
        all_ingredients |= set(ingredients)
        # get a list of the allergens and store a dict of allergens with the food it is
        # contained in (allergens_in_food[dairy] = {1, 2, 3...}
        allergens = line.split(' (')[1][9:-2].strip().split(', ')

        for a in allergens:
            if a not in possible_allergens:
                possible_allergens[a] = set(ingredients)
            else:
                possible_allergens[a] &= set(ingredients)

print()
print('Recipes:')
print(recipes)
print()
print('All ingredients:')
print(all_ingredients)
print()
print('Possible allergens:')
print(possible_allergens)

# Part 1: count occurence of each ingredient not a possible allergen in the recipes
all_possible_allergens = set((x for ing_set in possible_allergens.values() for x in ing_set))
no_allergens = all_ingredients - all_possible_allergens

part1 = 0
for ing in no_allergens:
    part1 += sum(1 for r in recipes if ing in r)

print(f'Part 1: {part1}')
