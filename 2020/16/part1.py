import re

rows = open('input', 'r').read().split('\n')
parseRule = re.compile('^([\w ]+): ((?:[0-9]+)-(?:[0-9]+)) or ((?:[0-9]+)-(?:[0-9]+))')

values = {}
i = 0
row = rows[i]

while ':' in row:
  rule = parseRule.findall(row)[0]
  field = rule[0]

  for rangeStr in [rule[1], rule[2]]:
    r = rangeStr.split('-')
    
    for j in range(int(r[0]), int(r[1]) + 1):
      values[j] = field

  i += 1
  row = rows[i]

validateTickets = False
errorRate = 0

while i < len(rows):
  row = rows[i]

  if validateTickets == True:
    ticketValues = row.split(',')
    
    for j in ticketValues:
      if int(j) not in values:
        errorRate += int(j)

  if row[0:6] == 'nearby':
    validateTickets = True

  i += 1

print(errorRate)

