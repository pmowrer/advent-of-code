import math

def parse(input):
  heightMap = []

  for line in input:
    heightMap += [[int(x) for x in line.replace('\n', '')]]

  return heightMap

def getNeighbors(heightMap, x, y):
  neighbors = []

  left = x - 1
  right = x + 1
  up = y - 1
  down = y + 1

  if left >= 0:
    neighbors += [[left, y]]

  if right < len(heightMap[y]):
    neighbors += [[right, y]]

  if up >= 0:
    neighbors += [[x, up]]

  if down < len(heightMap):
    neighbors += [[x, down]]

  return neighbors

def getPointId(x, y):
  return f'{x},{y}'

def getHeight(heightMap, x, y):
  return heightMap[y][x]

def getBasinSize(heightMap, x, y):
  points = [[x, y]]
  size = 0
  seen = { getPointId(x, y): True }

  while (len(points)) > 0:
    x, y = points.pop(0)

    if (getHeight(heightMap, x, y) != 9):
      size += 1
      unseenNeighbors = [p for p in getNeighbors(heightMap, x, y) if getPointId(p[0], p[1]) not in seen]
      
      for p in unseenNeighbors:
        seen[getPointId(p[0], p[1])] = True

      if len(unseenNeighbors) > 0:
        points += unseenNeighbors

  return size

with open('input', encoding="utf-8") as f:
  heightMap = parse(f)
  largestBasinSizes = []
  
  for y in range(0, len(heightMap)):
    for x in range(0, len(heightMap[y])):
      height = getHeight(heightMap, x, y)

      neighbors = getNeighbors(heightMap, x, y)

      isLowPoint = len([p for p in neighbors if getHeight(heightMap, p[0], p[1]) > height]) == len(neighbors)

      if (isLowPoint):
        basinSize = getBasinSize(heightMap, x, y)

        if len(largestBasinSizes) < 3:
          largestBasinSizes += [basinSize]
        else:
          insertIndex = None

          for i, s in enumerate(largestBasinSizes):
            if basinSize > s:
              insertIndex = i

          if insertIndex != None:
            largestBasinSizes = largestBasinSizes[0: insertIndex] + [basinSize] + largestBasinSizes[insertIndex + 1:]

  print(math.prod(largestBasinSizes))