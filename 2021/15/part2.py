from queue import PriorityQueue
import math

def parse(input):
  riskMap = []

  for line in input:
    riskMap += [[int(x) for x in line.replace('\n', '')]]

  return riskMap

def expandRiskMap(riskMap, size):
  oldSize = len(riskMap)
  newRiskMap = [None] * oldSize * size

  for y in range(len(newRiskMap)):
    newRiskMap[y] = [None] * oldSize * size

    for x in range(0, len(newRiskMap[y])):      
      v = riskMap[y % oldSize][x % oldSize]
      newV = v + math.floor(x / oldSize) + math.floor(y / oldSize)
 
      if newV > 9:
        newV = newV % 10 + 1

      newRiskMap[y][x] = newV

  return newRiskMap

with open('input', encoding="utf-8") as f:
  riskMap = parse(f)
  riskMap = expandRiskMap(riskMap, 5)
  size = len(riskMap)

  lowestRisk = { '0,0': 0 }
  unvisited = PriorityQueue()
  seen = { '0,0': True }

  unvisited.put((0, [0, 0]))

  while not unvisited.empty():
    risk, current = unvisited.get()

    x, y = current

    neighbors = [[x + n[0], y + n[1]] for n in [[1, 0], [0, 1], [-1, 0], [0, -1]] if x + n[0] < size and x + n[0] >= 0 and y + n[1] < size and y + n[1] >= 0]

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
    
