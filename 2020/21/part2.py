import re

parseRow = re.compile('^([a-z]+) (?:\(contains(?: ([a-z]+),?)+)?')

rows = open('input', 'r').read().split('\n')

allergensToFood = {}
foodCounts = {}
foodsToAllergens = {}
allFoods = []
allAllergens = []

for row in rows:
  x = row.split(' (contains ')
  foods = x[0].split(' ')
  allergens = x[1][:-1].split(', ')
  allFoods = set(allFoods).union(foods)
  allAllergens = set(allAllergens).union(allergens)

  for food in foods:
    if food not in foodCounts:
      foodCounts[food] = 0

    foodCounts[food] += 1

  # find intersection between all allergens => [food list]
  #for food in foods:
  #  foodsToAllergens[food] = allergens
  
  for allergen in allergens:
    if allergen not in allergensToFood:
      allergensToFood[allergen] = []

    allergensToFood[allergen].append(foods)

allergenFoods = []

found = {}

for allergen in allergensToFood:
  x = list(set(allergensToFood[allergen][0]).intersection(*allergensToFood[allergen]))
  z = [y for y in x if y not in found]
  allergensToFood[allergen] = z
  allergenFoods += z

  if len(z) == 1:
    found[z[0]] = allergen

for allergen in allergensToFood:
  z = [y for y in allergensToFood[allergen] if y not in found]
  allergensToFood[allergen] = z
  allergenFoods += z

  if len(z) == 1:
    found[z[0]] = allergen

for allergen in allergensToFood:
  z = [y for y in allergensToFood[allergen] if y not in found]
  allergensToFood[allergen] = z
  allergenFoods += z

  if len(z) == 1:
    found[z[0]] = allergen

for allergen in allergensToFood:
  z = [y for y in allergensToFood[allergen] if y not in found]
  allergensToFood[allergen] = z
  allergenFoods += z

  if len(z) == 1:
    found[z[0]] = allergen


invFound = {v: k for k, v in found.items()}
cdil = []

for allergen in sorted(allAllergens):
 cdil.append(invFound[allergen])

print('allergenFoods', allergensToFood)
print('allAllergens', sorted(allAllergens), cdil)
print('cdil', ','.join(cdil))

