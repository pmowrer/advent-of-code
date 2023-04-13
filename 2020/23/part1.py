from collections import deque

cups = [int(x) for x in '389125467']

i = 0
move = 0

while move < 100:
  p = [cups[(i + 1) % 9], cups[(i + 2) % 9], cups[(i + 3) % 9]]
  q = [x for x in cups if x not in p]
  j = 1
  d = ((cups[i] - 1) % 9)
  d = 9 if d == 0 else d
  c = cups[i]

  while d in p:
    d = ((d - 1) % 9) if d > 1 else 9

  di = q.index(d) 

  print('Move', move + 1, ['(' + str(x) + ')' if x == c else x for x in cups], 'i:', i, 'd:', d, 'p:', p, 'q:', q, 'di:', di)
 
  cups = deque(q[0:di + 1] + p + q[di + 1:])

  while cups.index(c) != i:
   cups.rotate(1)

  cups = list(cups)
  i = (i + 1) % 9
  move += 1

cups = deque(cups)

while cups[0] != 1:
  cups.rotate(1)

print(''.join([str(c) for c in cups])[1:])