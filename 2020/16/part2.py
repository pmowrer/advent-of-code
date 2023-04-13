import re

rows = open('input', 'r').read().split('\n')
parseRule = re.compile('^([\w ]+): ((?:[0-9]+)-(?:[0-9]+)) or ((?:[0-9]+)-(?:[0-9]+))')

valueToFields = {}
i = 0
row = rows[i]

while ':' in row:
  rule = parseRule.findall(row)[0]
  field = rule[0]

  for rangeStr in [rule[1], rule[2]]:
    r = rangeStr.split('-')
    
    for j in range(int(r[0]), int(r[1]) + 1):
      valueToFields[j] = [field] if j not in valueToFields else valueToFields[j] + [field]

  i += 1
  row = rows[i]

fields = []
found = {}
ticket = []
nextIsTicket = False

while i < len(rows):
  row = rows[i]
  ticketValues = row.split(',')

  if row[0:4] == 'your':
    nextIsTicket = True
  elif nextIsTicket == True:
    ticket = ticketValues
    nextIsTicket = False

  if len(ticketValues) > 1:
    newFields = []
    invalid = False
   
    for j, v in enumerate(ticketValues):
      if int(v) not in valueToFields:
        invalid = True
        break
      else:
        if len(fields) <= j:
          newValues = valueToFields[int(v)]
        else:
          newValues = [x for x in valueToFields[int(v)] if x in fields[j] and x not in found]

        if len(newValues) == 1:
          found[newValues[0]] = j

        newFields.append(newValues)

    if invalid != True:
      fields = newFields

  i += 1

while len(found) < 20:
  for j, v in enumerate(fields):
    newValues = [x for x in fields[j] if x not in found]

    if len(newValues) == 1:
      found[newValues[0]] = j

    fields[j] = newValues

n = 1

for j in found:
  if j[0:9] == 'departure':
    n *= int(ticket[found[j]])

print(n)
