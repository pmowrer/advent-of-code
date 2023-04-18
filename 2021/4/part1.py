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
        
  return [numbers, numberToCellIds, cellIdToNumber]

def playBingo(numbers, numberToCellIds, cellIdToNumber):
  bingoCounts = {}

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
        return [int(number), gridId, cellIdToNumber]

with open('input', encoding="utf-8") as f:
  numbers, numberToCellIds, cellIdToNumber = parse(f)

  winningNumber, winningGridId, unmarkedCells = playBingo(numbers, numberToCellIds, cellIdToNumber)

  unmarkedCellSum = 0

  for cellId in unmarkedCells:
    if cellId.split(',')[0] == winningGridId:
      unmarkedCellSum += int(unmarkedCells[cellId])

  print(unmarkedCellSum * winningNumber)


