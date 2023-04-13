rows = open('input', 'r').read().split('\n')

# track active cubes
# for each active cube, tag its neighbors
# map neighbor -> active cubes[]
# loop through neighbors:
#  neighbor is active
#    remove from inactive if cubes[] < 2 or > 3
#  neighbor is inactive
#    add to active if cubes[] === 3
# 

active = {}

for i, row in enumerate(rows):
  for j, v in enumerate(row):
    if v == '#':
      active[','.join([str(j), str(i), '0', '0'])] = True

def getNeighbors(cube):
  neighbors = []
  points = [int(c) for c in cube.split(',')]
  
  for x in [-1, 0, 1]:
    for y in [-1, 0, 1]:
      for z in [-1, 0, 1]:
        for w in [-1, 0, 1]:
          if not (x == 0 and y == 0 and z == 0 and w == 0):
            neighbor = ','.join(
              [str(i) for i in [points[0] + x, points[1] + y, points[2] + z, points[3] + w]]
            )
            neighbors.append(neighbor)

  return neighbors

def runCycle():
  deactivateQueue = []
  inactiveNeighbors = {}

  for activeCube in active:
    activeNeighbors = 0

    for nCube in getNeighbors(activeCube):
      if nCube in active:
        activeNeighbors += 1
      else:
        if nCube in inactiveNeighbors:
          inactiveNeighbors[nCube].append(activeCube)
        else:
          inactiveNeighbors[nCube] = [activeCube]
      
    if activeNeighbors not in [2, 3]:
      deactivateQueue.append(activeCube)

  while len(deactivateQueue) > 0:
    del active[deactivateQueue.pop()]

  for neighbor in inactiveNeighbors:
    if len(inactiveNeighbors[neighbor]) == 3:
      active[neighbor] = True
  

cycle = 0

while cycle < 6:
  runCycle()
  cycle +=1

print(len(active))