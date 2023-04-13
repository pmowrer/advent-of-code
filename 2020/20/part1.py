rows = open('input', 'r').read().split('\n')

tileId = 0

# parse tile edges, insides don't matter
# parse edges into string
# find matching edges across tiles
# hopefully there are unique pairs
# from there, eliminate known pairs from all other matches
#

edges = {}
i = 0

while i < len(rows):
  row = rows[i]

  if len(row) > 0 and row[0] == 'T':
    tileId = row[5:9]
    j = 1
    t = rows[i + 1]
    b = rows[i + 10]
    l = ''
    r = ''

    while j <= 10 and rows[i + j][0] in ['.', '#']:
      l += rows[i + j][0]
      r += rows[i + j][len(row) - 1]
      j += 1

    print([len(x) for x in [t, b, l, r]])
    tileEdges = [t, b, l, r]
    tileEdges += [x[::-1] for x in tileEdges]
    edges[tileId] = [int(x.replace('#', '1').replace('.', '0'), 2) for x in tileEdges]
    i += j
   
  i += 1

matches = {}

print(edges)

for tileId in edges:
  for tileId2 in edges:
    if tileId != tileId2:
      intersect = list(set(edges[tileId]) & set(edges[tileId2]))

      if len(intersect) > 0:
        matches[tileId] = list(set(matches[tileId] + [tileId2])) if tileId in matches else [tileId2]
        matches[tileId2] = list(set(matches[tileId2] + [tileId])) if tileId2 in matches else [tileId]

min = 0
corners = []

for match in matches:
  count = len(matches[match])

  if count < min or min == 0:
    min = count
    corners = [match]
  elif count == min:
    corners.append(match)

i = 0
total = 1

while i < len(corners):
  total *= int(corners[i])
  i += 1

#  print(match, len(matches[match]))

print(corners, total)