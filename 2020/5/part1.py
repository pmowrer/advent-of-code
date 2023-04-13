rows = open('input', 'r').read().split('\n')
hi = 0

for row in rows:
    binRow = row[0:-3].replace('F', '0').replace('B', '1')
    binCol = row[-3:].replace('L', '0').replace('R', '1')

    rowNumber = int(binRow, 2)
    colNumber = int(binCol, 2)
    seatId = rowNumber * 8 + colNumber
    
    if hi < seatId:
        hi = seatId

print(hi)

