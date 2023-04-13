from collections import deque

rows = open('input', 'r').read().split('\n')

moves = { 'E': 0, 'N': 0, 'S': 0, 'W': 0 }
waypoint = { 'E': 10, 'N': 1, 'S': 0, 'W': 0 }
order = deque(['N', 'E', 'S', 'W'])

for row in rows:
  command = row[0:1]
  amount = int(row[1:])

  if command in ['N', 'S', 'E', 'W']:
    waypoint[command] += amount
  elif command in ['L', 'R']:
    steps = int(amount / 90)
    oldOrder = order.copy()

    order.rotate(steps * (1 if command == 'R' else -1))
    
    waypoint = { 
      'E': waypoint[order[oldOrder.index('E')]],
      'N': waypoint[order[oldOrder.index('N')]],
      'S': waypoint[order[oldOrder.index('S')]], 
      'W': waypoint[order[oldOrder.index('W')]] 
    }

  elif command == 'F':
    xdir = 'E' if waypoint['E'] > waypoint['W'] else 'W'
    ydir = 'N' if waypoint['N'] > waypoint['S'] else 'S'

    moves[xdir] += abs(waypoint['E'] - waypoint['W']) * amount
    moves[ydir] += abs(waypoint['N'] - waypoint['S']) * amount

x = abs(moves['E'] - moves['W'])
y = abs(moves['N'] - moves['S'])

print(moves, x, y, x + y)
