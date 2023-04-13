rows = open('input', 'r').read().split('\n')

def applyRules(grid):
  newGrid = []

  for i, row in enumerate(grid):
    newGrid.append([])

    for j, seat in enumerate(row):
      newGrid[i].append(seat)
      occupiedCount = 0

      roomLeft = j > 0
      roomRight = j < len(row) - 1
      roomUp = i > 0
      roomDown = i < len(grid) - 1
      
      # L    
      if roomLeft and row[j - 1] == '#':
        occupiedCount += 1

      # LU
      if roomLeft and roomUp and grid[i - 1][j - 1] == '#':
        occupiedCount += 1
      
      # LD
      if roomLeft and roomDown and grid[i + 1][j - 1] == '#':
        occupiedCount += 1

      # R
      if roomRight and row[j + 1] == '#':
        occupiedCount += 1

      # RU
      if roomRight and roomUp and grid[i - 1][j + 1] == '#':
        occupiedCount += 1

      # RD
      if roomRight and roomDown and grid[i + 1][j + 1] == '#':
        occupiedCount += 1

      # U
      if roomUp and grid[i - 1][j] == '#':
        occupiedCount += 1

      # D
      if roomDown and grid[i + 1][j] == '#':
        occupiedCount += 1

      if seat == 'L' and occupiedCount == 0:
        newGrid[i][j] = '#'
      elif seat == '#' and occupiedCount >= 4:
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