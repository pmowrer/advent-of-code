def parse(input):
  numbers = []
  numberToCellIds = {}
  cellIdToNumber = {}
  gridCount = 0
  rowCount = 0

  for i, line in enumerate(input):
    line = line.replace('\n', '')

    if i == 0:
      numbers = line.split(',') 
    elif (i - 1) % 6 == 0:
      gridCount += 1
      rowCount = 0
    else:
      rowCount += 1

      for i, number in enumerate(line.split()):
        cellId = f'g{gridCount},r{rowCount},c{i}';

        numberToCellIds.setdefault(number, [])
        numberToCellIds[number] += [cellId]

        cellIdToNumber[cellId] = number
        
  return [numbers, numberToCellIds, cellIdToNumber, gridCount]

def playBingo(numbers, numberToCellIds, cellIdToNumber, gridCount):
  bingoCounts = {}
  winningGrids = {}
  winningGridCount = 0

  for number in numbers:
    cellIds = numberToCellIds[number]

    for cellId in cellIds:
      gridId, rowId, columnId = cellId.split(',')

      rowCountId = f'{gridId}{rowId}'
      columnCountId = f'{gridId}{columnId}'

      bingoCounts[rowCountId] = bingoCounts.get(rowCountId, 0) + 1
      bingoCounts[columnCountId] = bingoCounts.get(columnCountId, 0) + 1

      del cellIdToNumber[cellId]

      if bingoCounts[rowCountId] == 5 or bingoCounts[columnCountId] == 5:
        if gridId not in winningGrids:
          winningGrids[gridId] = True
          winningGridCount += 1

        if winningGridCount == gridCount:
          return [int(number), gridId, cellIdToNumber]

def getUnmarkedCellSum(winningGridId, unmarkedCells):
  unmarkedCellSum = 0

  for cellId in unmarkedCells:
    if cellId.split(',')[0] == winningGridId:
      unmarkedCellSum += int(unmarkedCells[cellId])

  return unmarkedCellSum

with open('input', encoding="utf-8") as f:
  numbers, numberToCellIds, cellIdToNumber, gridCount = parse(f)

  lastWinningNumber, lastWinningGridId, unmarkedCells = playBingo(numbers, numberToCellIds, cellIdToNumber, gridCount)

  unmarkedCellSum = getUnmarkedCellSum(lastWinningGridId, unmarkedCells)

  print(unmarkedCellSum * lastWinningNumber)


