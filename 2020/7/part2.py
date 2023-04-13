import re

parseRule = re.compile('^(\w+ \w+)(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?')

rules = open('input', 'r').read().split('\n')
bags = {}

for rule in rules:
  parsed = parseRule.match(rule).groups()
  bag = parsed[0]
  contents = parsed[1:]

  bags[bag] = [{ 'count': int(content[0]), 'color': content[2:] } for content in contents if content != None]

def findBagCount(bagColor):
  count = 0
  containedBags = bags[bagColor]

  for containedBag in containedBags:
    count += containedBag['count'] * (1 + findBagCount(containedBag['color']))
  
  return count

print(findBagCount('shiny gold'))

