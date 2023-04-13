rows = open('input', 'r').read().split('\n')

def isFirstVisibleSeatOccupied(grid, i, j, dir):
  x = j
  y = i
  done = False

  while done is False:
    roomLeft = x > 0
    roomRight = x < len(grid[y]) - 1
    roomUp = y > 0
    roomDown = y < len(grid) - 1

    if dir == 'U' and roomUp:
      y -= 1
    elif dir == 'D' and roomDown:
      y += 1
    elif dir == 'L' and roomLeft:
      x -= 1
    elif dir == 'R' and roomRight:
      x += 1
    elif dir == 'UL' and roomLeft and roomUp:
      x -= 1
      y -= 1
    elif dir == 'UR' and roomRight and roomUp:
      x += 1
      y -= 1
    elif dir == 'DL' and roomLeft and roomDown:
      x -= 1
      y += 1
    elif dir == 'DR' and roomRight and roomDown:
      x += 1
      y += 1
    else:
      done = True

    if grid[y][x] != '.':
      done = True

  return (x != j or y != i) and grid[y][x] == '#'

def applyRules(grid):
  newGrid = []

  for i, row in enumerate(grid):
    newGrid.append([])

    for j, seat in enumerate(row):
      newGrid[i].append(seat)
      occupiedCount = 0

      for dir in ['U', 'D', 'L', 'R', 'UL', 'UR', 'DL', 'DR']:
        if isFirstVisibleSeatOccupied(grid, i, j, dir):
          occupiedCount += 1

      if seat == 'L' and occupiedCount == 0:
        newGrid[i][j] = '#'
      elif seat == '#' and occupiedCount >= 5:
        newGrid[i][j] = 'L'

  return newGrid

rounds = 1
seats = applyRules(rows)

while True:
  newSeats = applyRules(seats)

  if newSeats == seats:
    break
  else:
    rounds += 1
    seats = newSeats

occupiedCount = 0

for i, row in enumerate(seats):
  for j, seat in enumerate(row):
    if seat == '#':
      occupiedCount += 1

print(occupiedCount)