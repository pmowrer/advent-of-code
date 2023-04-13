rows = open('input', 'r').read().split('\n')

player1 = []
player2 = []
current = player1

for row in rows:
  if len(row) > 0:
    if row[0] != 'P':
     current += [int(row)]
    elif row == 'Player 2:':
      current = player2

player1 = player1[::-1]
player2 = player2[::-1]
r = 0

while len(player1) > 0 and len(player2) > 0:
  c1 = player1.pop()
  c2 = player2.pop()

  if c1 > c2:
    player1 = [c2, c1] + player1
  else:
    player2 = [c1, c2] + player2

  r += 1

t1 = 0
t2 = 0

for i, p in enumerate(player1):
  t1 += (i + 1) * p

for i, p in enumerate(player2):
  t2 += (i + 1) * p

print(t1, t2)
