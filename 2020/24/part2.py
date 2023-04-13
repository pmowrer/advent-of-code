import re
 
parseMoves = re.compile('(e|se|sw|w|nw|ne)')

rows = open('input', 'r').read().split('\n')
tiles = {}

print(len(rows))

for row in rows:
  x = 0.0
  y = 0.0
  instructions = parseMoves.findall(row)

  for i in instructions:
    if i == 'e':
      x += -1
    elif i == 'se':
      x += -0.5
      y += -1
    elif i == 'sw':
      x += 0.5
      y += -1
    elif i == 'w':
      x += 1
    elif i == 'nw':
      x += 0.5
      y += 1
    elif i == 'ne':
      x += -0.5
      y += 1

  p = ','.join([str(x), str(y)])
  tiles[p] = 0 if p in tiles else 1

i = 0

# print(tiles)

# newTiles = {}

# for tile in tiles:
#   newTiles[tile] = tiles[tile]
#   t = tile.split(',')
#   adj = [[-1, 0], [-0.5, -1], [0.5, -1], [1, 0], [0.5, 1], [-0.5, 1]]

#   for a in adj:
#     x = float(t[0]) + a[0]
#     y = float(t[1]) + a[1]
#     p = ','.join([str(x), str(y)])
#     newTiles[p] = tiles[p] if p in tiles else 0

# tiles = newTiles

# print(tiles)

print('start', i, len([t for t in tiles if tiles[t] == 1]))

while i < 100:
  newTiles = {}


  for tile in tiles:
    newTiles[tile] = tiles[tile]
    t = tile.split(',')
    adj = [[-1, 0], [-0.5, -1], [0.5, -1], [1, 0], [0.5, 1], [-0.5, 1]]

    for a in adj:
      x = float(t[0]) + a[0]
      y = float(t[1]) + a[1]
      p = ','.join([str(x), str(y)])
      newTiles[p] = tiles[p] if p in tiles else 0

  tiles = newTiles
  newTiles = {}

  for tile in tiles:
    b = 0
    adj = [[-1, 0], [-0.5, -1], [0.5, -1], [1, 0], [0.5, 1], [-0.5, 1]]

    for a in adj:
      t = tile.split(',')
      x = float(t[0]) + a[0]
      y = float(t[1]) + a[1]
      p = ','.join([str(x), str(y)])
#      print('p', p)

      if p in tiles and tiles[p] == 1:
        b += 1

    if tiles[tile] == 1 and b not in [1, 2]:
      newTiles[tile] = 0
    elif tiles[tile] == 0 and b == 2:
      newTiles[tile] = 1
    else:
      newTiles[tile] = tiles[tile]

#    print('tile', tiles[tile], newTiles[tile], 'blacks', b, newTiles)
  
 # print(i, len(newTiles), len([t for t in newTiles if newTiles[t] == 1]))

  tiles = newTiles
  print(i, len([t for t in tiles if tiles[t] == 1]))
  i += 1
