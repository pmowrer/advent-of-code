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

def sumDeck(d):
  t = 0

  for i, c in enumerate(d):
    t += (i + 1) * c

  return t

def combat(p1, p2):
  rounds = {}

  while len(p1) > 0 and len(p2) > 0:
    sum1 = sumDeck(p1)
    sum2 = sumDeck(p2)

    if sum1 in rounds and sum2 in rounds[sum1]:
      return [p1, []]

    rounds[sum1] = list(set(rounds[sum1] + [sum2])) if sum1 in rounds else [sum2]

    c1 = p1.pop()
    c2 = p2.pop()

    if c1 <= len(p1) and c2 <= len(p2):      
      winner = p1 if combat(p1[-c1:], p2[-c2:])[0] != [] else p2
    else:
      winner = p1 if c1 > c2 else p2

    if winner == p1:
      p1 = [c2, c1] + p1
    else:
      p2 = [c1, c2] + p2

  return [p1, p2]

res = combat(player1, player2)

print(sumDeck(res[0]), sumDeck(res[1]))
