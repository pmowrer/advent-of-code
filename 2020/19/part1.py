rows = open('input', 'r').read().split('\n')

rules = {}
res = {}
messages = []
maxMessageLen = 0

for row in rows:
  if len(row) > 0: 
    if row[0] in ['a', 'b']:
      messages.append(row)

      if len(row) > maxMessageLen:
        maxMessageLen = len(row)
    else:
      i = int(row[0:row.index(':')])
      rules[i] = [x.strip().replace('"', '').replace(' ', ',') for x in row[row.index(':') + 1:].split('|')]

q = rules[0]

while len(q) > 0:
  print(len(res))
  x = q.pop().split(',')
  y = 0

  while y < len(x) and x[y] in ['a', 'b']:
    y += 1

  match = False

  for m in messages:
    if m.startswith(''.join(x[0:y])) == True:
      match = True
      break

  if match and len(x) <= maxMessageLen:
    if y == len(x):
      res[''.join(x)] = True
    else:
      [q.append(','.join(x[0:y] + z.split(',') + x[y+1:])) for z in rules[int(x[y])]]

c = 0

for m in messages:
  if m in res:
    c += 1

print(res, c)

