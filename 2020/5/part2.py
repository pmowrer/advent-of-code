rows = open('input', 'r').read().split('\n')

def getSeatId(row):
    binRow = row[0:-3].replace('F', '0').replace('B', '1')
    binCol = row[-3:].replace('L', '0').replace('R', '1')
    rowNumber = int(binRow, 2)
    colNumber = int(binCol, 2)
    seatId = rowNumber * 8 + colNumber
    return seatId

seatIds = [getSeatId(row) for row in rows]
seatIds.sort()

for i, seatId in enumerate(seatIds):
    if i > 0 and i < len(seatIds) and seatId - 1 != seatIds[i - 1]:
        print('missing', seatIds[i - 1], seatId, seatIds[i + 1])

