from collections import defaultdict
import math

def parse(input):
  template = []
  rules = {}

  for i, line in enumerate(input):
    line = line.replace('\n', '')

    if i == 0:
      template = [t for t in line]

    if i > 1:
      pair, element = line.split(' -> ')
      rules[pair] = element

  return template, rules

def getNewPairs(pair, rules):
  insertedElement = rules[pair]

  return [pair[0] + insertedElement, insertedElement + pair[1]]

def getElementCounts(pairCounts):
  elementCounts = defaultdict(int)

  for pair, count in pairCounts.items():
    for element in pair:
      elementCounts[element] += count

  for element, count in elementCounts.items():
    elementCounts[element] = math.ceil(count / 2)

  return elementCounts

with open('input', encoding="utf-8") as f:
  template, rules = parse(f)
  pairCounts = defaultdict(int)

  for i, t in enumerate(template):
    if i < len(template) - 1:
      pair = t + template[i + 1]
      pairCounts[pair] += 1

  for step in range(0, 40):
    newPairCounts = defaultdict(int)

    for pair, count in pairCounts.items():
      if count > 0:
        newPairs = getNewPairs(pair, rules)

        for newPair in newPairs:
          newPairCounts[newPair] += count

    pairCounts = newPairCounts

  elementCounts = getElementCounts(pairCounts)

  maxCount = 0
  minCount = 0

  for element, count in elementCounts.items():
    if count > maxCount:
      maxCount = count

    if minCount == 0 or count < minCount:
      minCount = count
  
  print(maxCount - minCount)
