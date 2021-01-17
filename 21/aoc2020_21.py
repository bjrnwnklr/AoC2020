from collections import defaultdict

# f_name = 'ex1.txt'
f_name = 'input.txt'

food = defaultdict(set)
allergens_in_food = defaultdict(list)
possible_ingredients = defaultdict(set)
all_ingredients = set()

with open(f_name, 'r') as f:
    for i, line in enumerate(f.readlines()):
        # get a list of the ingredients and record the food recipe as a set of the
        # ingredients (food[1] = ['aaaa', 'bbbb' etc]
        ingredients = line.split(' (')[0].strip().split()
        # get a list of the allergens and store a dict of allergens with the food it is
        # contained in (allergens_in_food[dairy] = {1, 2, 3...}
        allergens = line.split(' (')[1][9:-2].strip().split(', ')
        for a in allergens:
            allergens_in_food[a].append(set(ingredients))
            food[i] = set(ingredients)
        # store a dictionary of each ingredient and what allergens it could possibly be
        for ing in ingredients:
            all_ingredients.add(ing)
        # store a dictionary of each allergen and what food ingredient it could be
        for alg in allergens:
            possible_ingredients[alg] |= set(ingredients)


# print out what we have
print()
print('Food:')
for f in food:
    print(f'{f}: {food[f]}')
print()
print(f'All ingredients: {all_ingredients}')
print()
print('Allergens in food:')
for a in allergens_in_food:
    print(f'{a}: {allergens_in_food[a]}')
print()
print('Possible ingredients:')
for p in possible_ingredients:
    print(f'{p}: {possible_ingredients[p]}')

# take the difference of "possible ingredients" (all ingredients that could be an allergen
# with each of the food recipes containing the allergen

possible_allergens = defaultdict(set)
print()
print('These ingredients are possibly allergens because they show up in each recipe with the allergen.')
for alg in allergens_in_food:
    for ing in possible_ingredients[alg]:
        if all(ing in recipe for recipe in allergens_in_food[alg]):
            possible_allergens[ing].add(alg)
print(possible_allergens)

for ing in possible_allergens:
    all_ingredients.remove(ing)

print()
print(f'Ingredients that cant be allergen: {all_ingredients}')

# count how many times the remaining allergens show up in the recipes (stored in food)
part1 = 0
for ing in all_ingredients:
    part1 += sum(1 for recipe in food.values() if ing in recipe)

print()
print(f'Part 1: {part1}')

# part 1: 2584
