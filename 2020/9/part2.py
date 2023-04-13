rows = open('input', 'r').read().split('\n')
r = 0
preamble = 25

def getNumbersHash(index, preamble):
  numbers = {}

  for row in rows[i:i+preamble]:
    numbers[row] = int(row)
  
  return numbers


for i, row in enumerate(rows[preamble:]):
  r = 0
  numbers = getNumbersHash(i, preamble)

  for n in numbers:
    if r is not 0:
      break
    
    remainder = int(row) - int(n)

    if str(remainder) in numbers:
      r = row

  if r is 0:
    break

invalid = int(row)
ranges = []

print(invalid)

for i, row in enumerate(rows):
  end = 0
  total = 0
  range = [] 
  j = i

  while total < invalid:
    range += [int(rows[j])]
    total += int(rows[j])

    if total == invalid:
      print('equal!', range)
      ranges += range
      break;

    j += 1

  # print(row, total, invalid, range)
ranges.sort()

print(ranges, ranges[0] + ranges[len(ranges) - 1])

3145218 + 865846 