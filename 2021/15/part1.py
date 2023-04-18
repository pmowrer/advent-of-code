from queue import PriorityQueue

def parse(input):
  riskMap = []

  for line in input:
    riskMap += [[int(x) for x in line.replace('\n', '')]]

  return riskMap

with open('input', encoding="utf-8") as f:
  riskMap = parse(f)
  size = len(riskMap)

  lowestRisk = { '0,0': 0 }
  unvisited = PriorityQueue()
  seen = { '0,0': True }

  unvisited.put((0, [0, 0]))

  while not unvisited.empty():
    risk, current = unvisited.get()

    x, y = current

    neighbors = [[x + n[0], y + n[1]] for n in [[1, 0], [0, 1]] if x + n[0] < size and y + n[1] < size]

    for n in neighbors:
      nx, ny = n
      nid = f'{nx},{ny}'
      nRisk = risk + riskMap[ny][nx]

      if not nid in lowestRisk or nRisk < lowestRisk[nid]:
        lowestRisk[nid] = nRisk

      if nid not in seen:
        seen[nid] = True
        unvisited.put((nRisk, n))
  
  print(lowestRisk[f'{size - 1},{size - 1}'])
    
