def parse(input):
  lines = []

  for line in input:
    lines += [[int(x) for x in line.replace('\n', '')]]

  return lines

def findNeighbors(grid, x, y):
  neighbors = []
  potentialNeighbors = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1], [x - 1, y - 1], [x - 1, y + 1], [x + 1, y - 1], [x + 1, y + 1]]

  for n in potentialNeighbors:
    x, y = n

    if x >= 0 and y >= 0 and y < len(grid) and x < len(grid[y]):
      neighbors += [[x, y]]

  return neighbors

def getPointId(x, y):
  return f'{x},{y}'
  
with open('input', encoding="utf-8") as f:
  grid = parse(f)
  flashing = []
  flashCount = 0

  for i in range(0, 100):
    seen = {}

    for y, line in enumerate(grid):
      for x, p in enumerate(line):
        energy = grid[y][x]

        if energy == 9:
          flashing += [[x, y]]
          seen[getPointId(x, y)] = True
        else:
          grid[y][x] += 1

    while (len(flashing) > 0):
      flashCount += 1
      x, y = flashing.pop()
      grid[y][x] = 0
      neighbors = [p for p in findNeighbors(grid, x, y) if not getPointId(p[0], p[1]) in seen]

      for n in neighbors:
        x, y = n
        energy = grid[y][x]

        if energy == 9:
          flashing += [[x, y]]
          seen[getPointId(x, y)] = True
        elif energy != 0:
          grid[y][x] += 1

  print(flashCount)