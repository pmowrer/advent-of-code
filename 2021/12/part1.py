from multiprocessing import connection


def parse(input):
  connections = {}

  for line in input:
    b, e = line.replace('\n', '').split('-')

    connections.setdefault(b, []);
    connections.setdefault(e, []);

    connections[b] += [e]
    connections[e] += [b]

  return connections

def findEnd(connections, start, path = [], seen = {}):
  connectionsFromCurrent = connections[start]
  paths = []

  newPath = path + [start]
  
  if not start.isupper():
    seen[start] = True
  
  for connection in connectionsFromCurrent:
    if connection == 'end':
      paths += newPath + [connection]
    elif connection not in seen:
      paths += findEnd(connections, connection, newPath, seen.copy()) 

  return paths
  
with open('input', encoding="utf-8") as f:
  connections = parse(f)

  paths = findEnd(connections, 'start')
  pathCount = 0

  for path in paths:
    if path == 'start':
      pathCount += 1

  print(pathCount)