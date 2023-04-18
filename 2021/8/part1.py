from collections import defaultdict

def parseOutputValues(input):
  values = []

  for line in input:
    values += line.replace('\n', '').split(' | ')[1].split(' ')

  return values

with open('input', encoding="utf-8") as f:
  values = parseOutputValues(f)
  count = 0

  for value in values:
    l = len(value)

    if l == 2 or l == 3 or l == 4 or l == 7:
      count += 1

  print(count)
  
