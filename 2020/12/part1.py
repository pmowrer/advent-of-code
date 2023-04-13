rows = open('input', 'r').read().split('\n')

dir = 'E'
order = ['N', 'E', 'S', 'W']
moves = { 'E': 0, 'N': 0, 'S': 0, 'W': 0 }

for row in rows:
  command = row[0:1]
  amount = int(row[1:])

  if command in ['N', 'S', 'E', 'W']:
    moves[command] += amount
  elif command in ['L', 'R']:
    steps = int(amount / 90)
    dir = order[(order.index(dir) + steps * (-1 if command == 'L' else 1)) % 4]
  elif command == 'F':
    moves[dir] += amount

x = abs(moves['E'] - moves['W'])
y = abs(moves['N'] - moves['S'])

print(x + y)

    


