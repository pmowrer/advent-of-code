import re
 
parseMoves = re.compile('(e|se|sw|w|nw|ne)')

rows = open('input', 'r').read().split('\n')
tiles = {}

print(len(rows))

for row in rows:
  x = 0
  y = 0
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

  if p in tiles:
    del tiles[p]
    print('SEEN', p)
  else:
    tiles[p] = True

  print(p)

print(len(tiles))
