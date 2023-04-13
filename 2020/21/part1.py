import re

parseRow = re.compile('^([a-z]+) (?:\(contains(?: ([a-z]+),?)+)?')

rows = open('input', 'r').read().split('\n')

allergensToFood = {}
foodCounts = {}
foodsToAllergens = {}
allFoods = []

for row in rows:
  print(row)
  x = row.split(' (contains ')
  foods = x[0].split(' ')
  allergens = x[1][:-1].split(', ')
  allFoods = set(allFoods).union(foods)

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

for allergen in allergensToFood:
  allergensToFood[allergen] = set(allergensToFood[allergen][0]).intersection(*allergensToFood[allergen])
  allergenFoods += allergensToFood[allergen]

print(allergensToFood)
print(allFoods)
print('allergenFoods', allergenFoods)

excluded = set(allFoods) - set(allergenFoods)
total = 0

for e in excluded:
  total += foodCounts[e]

print(total)