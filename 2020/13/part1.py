rows = open('input', 'r').read().split('\n')

depart = int(rows[0])
closestBusId = 0
closestT = 100000

for busId in rows[1].split(','):
  if busId != 'x':
    inServiceBusId = int(busId)
    t = int(round((1 - ((depart / float(busId)) % 1)) * inServiceBusId))

    if t < closestT:
      closestBusId = int(busId)
      closestT = t

print(closestT * closestBusId)