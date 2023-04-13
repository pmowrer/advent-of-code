from collections import deque

rows = open('exampleinput', 'r').read().split('\n')

tileId = 0
edges = {}
tiles = {}
i = 0

while i < len(rows):
  row = rows[i]

  if len(row) > 0 and row[0] == 'T':
    tileId = row[5:9]
    j = 1
    tile = []

    while j <= 10 and rows[i + j][0] in ['.', '#']:
      tile.append(rows[i + j])
      j += 1

    tiles[tileId] = tile
    tileEdges = [tile[0], ''.join([t[9] for t in tile]), tile[9], ''.join([t[0] for t in tile])]

    # critical to append reversed tileEdges to emulate flipped/rotated tile matches below
    tileEdges += [x[::-1] for x in tileEdges]
    edges[tileId] = tileEdges    
    i += j
   
  i += 1

r = int(len(tiles)**(.5))
matches = {}

for tileId1 in edges:
  if tileId1 not in matches:
    matches[tileId1] = ['' * 8 for i in range(8)]
  
  for tileId2 in edges:
    if tileId2 not in matches:
      matches[tileId2] = ['' * 8 for i in range(8)]

    if tileId1 != tileId2:
      matching1 = [e if e in edges[tileId1] else '' for i, e in enumerate(edges[tileId2])]
      matching2 = [e if e in edges[tileId2] else '' for i, e in enumerate(edges[tileId1])]

      matches[tileId1] = [tileId2 if e in edges[tileId2] else matches[tileId1][i] for i, e in enumerate(edges[tileId1])]
      matches[tileId2] = [tileId1 if e in edges[tileId1] else matches[tileId2][i] for i, e in enumerate(edges[tileId2])]

borders = []
corners = []
middles = []

for match in matches:
  count = len([m for m in matches[match][0:4] if m != ''])

  if count == 2:
    corners.append(match)
  elif count == 3:
    borders.append(match)
  elif count == 4:
    middles.append(match)

img = [[0] * r for i in range(r)]
used = {}
i = 0

while i < r:
  j = 0

  while j < r:
    if i % (r - 1) == 0 and j % (r - 1) == 0:
      possible = corners
    elif i % (r - 1) == 0 or j % (r - 1) == 0:
      possible = borders
    else:
      possible = middles

    neighbors = ([img[i - 1][j]] if i > 0 else []) + ([img[i][j - 1]] if j > 0 else [])
    neighborMatches = set.intersection(*[set(x) for x in [matches[x][0:4] for x in neighbors]]) if len(neighbors) > 0 else []

    tileId = [p for p in possible if len(neighborMatches) == 0 or (p in neighborMatches and p not in used)][0]
    tile = tiles[tileId]
    img[i][j] = tileId
    used[tileId] = True
    j += 1

  i += 1

actual = ['' * r for i in range(r * 8)]
i = 0

while i < r:
  j = 0

  while j < r:
    tileId = img[i][j]
    tile = tiles[tileId]
    tileMatches = deque([m for m in matches[tileId][0:4]])

    k = 0

    up = img[i - 1][j] if i > 0 else ''
    down = img[i + 1][j] if i < (r - 1) else ''
    left = img[i][j - 1] if j > 0 else ''
    right = img[i][j + 1] if j < (r - 1) else ''

    while tileMatches[0] != up or tileMatches[1] != right or tileMatches[2] != down or tileMatches[3] != left:
      if k == 4:
        # flip vertical
        tile.reverse()
        tileMatches = deque([tileMatches[2], tileMatches[1], tileMatches[0], tileMatches[3]])
      elif k == 8:
        # flip horizontal
        tile = [t[::-1] for t in tile]
        tileMatches = deque([tileMatches[0], tileMatches[3], tileMatches[2], tileMatches[1]])
      else:
        # rotate
        tile = [''.join(r) for r in list(zip(*tile[::-1]))]
        tileMatches.rotate(1)

      k += 1
  
    tiles[tileId] = tile
  
    k = 0
    
    while k < 8:
      actual[(i * 8) + k] += tile[k + 1][1:9]
      k += 1
  
    j += 1

  i += 1

print('\n'.join(x for x in actual))

def toBin(row):
  return bin(int(row.replace('.', '0').replace('#', '1'), 2))

monster = ['..................#.', '#....##....##....###', '.#..#..#..#..#..#...']
monsterbin = [toBin(x) for x in monster]

def findSeaMonster(img):
  i = 0

  while i < len(img) - 2:
    print(toBin(img[i]), monsterbin[0], bin(toBin(img[i]) & monsterbin[0]))
    matches1 = bin(toBin(img[i]) & monsterbin[0]) == bin(monsterbin[0])
    matches2 = bin(toBin(img[i + 1]) & monsterbin[1]) == bin(monsterbin[1])
    matches3 = bin(toBin(img[i + 2]) & monsterbin[2]) == bin(monsterbin[2])

    # sub binary representation of each monster row from rows
    if matches1 and matches2 and matches3:
      return True
  
    i += 1

  return False
  
found = False
k = 0

while found != True:
  found = findSeaMonster(actual)

  if k == 4:
    # flip vertical
    actual.reverse()
  elif k == 8:
    # flip horizontal
    actual = [t[::-1] for t in actual]
  else:
    # rotate
    actual = [''.join(r) for r in list(zip(*actual[::-1]))]

print('FOUND')


print(findSeaMonster(actual))