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
  
with open('input', encoding="utf-8") as f:
  coords, folds = parse(f)

  seenCoords = {}
  newCoords = []

  d, n = folds[0]

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

  print(len(newCoords))