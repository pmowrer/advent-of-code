def parse(input):
  coords = []
  folds = []

  for line in input:
    if line[0] == 'f':
      d, n = line.replace('\n', '').split('=')
      folds += [[d[-1:], int(n)]]
    elif len(line) > 1:
      coords += [[int(x) for x in line.replace('\n', '').split(',')]]

  return coords, folds

def getCoordId(coord):
  x, y = coord
  return f'{x},{y}'

def printCoords(coords):
  coordsDict = {}

  for coord in coords:
    x, y, = coord
    coordsDict[f'{x},{y}'] = True

  width = 40
  height = 6

  print('\n'.join([''.join(['{:3}'.format('#' if f'{x},{y}' in coordsDict else '.') for x in range(width)]) 
    for y in range(height)]))

with open('input', encoding="utf-8") as f:
  coords, folds = parse(f)

  for fold in folds:
    newCoords = []
    seenCoords = {}

    d, n = fold

    for coord in coords:
      x, y = coord

      if d == 'x':
        foldedCoord = [abs(x - n * 2) if x > n else x, y]
      else:
        foldedCoord = [x, abs(y - n * 2) if y > n else y]

      foldedCoordId = getCoordId(foldedCoord)

      if foldedCoordId not in seenCoords:
        newCoords += [foldedCoord]
        seenCoords[foldedCoordId] = True

    coords = newCoords

  printCoords(coords)