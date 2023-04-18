from collections import defaultdict

def parse(input):
  for line in input:
    return [int(x) for x in line.replace('\n', '').split(',')]

with open('input', encoding="utf-8") as f:
  min = None
  max = None
  minFuel = None

  positions = defaultdict(int)

  for position in parse(f):
    positions[position] += 1

    if not min or position < min:
      min = position
    
    if not max or position > max:
      max = position

  for i in range(min, max):
    fuel = 0

    for k, v in positions.items():
      if minFuel and fuel >= minFuel:
        break

      fuel += abs(i - k) * v

    if not minFuel or fuel < minFuel:
      minFuel = fuel
      
  print(minFuel)
