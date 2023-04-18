def getPositionBit(numbers, position, inverse = False):
  ones = [bits for bits in numbers if int(bits[position]) > 0]
  sign = (1 if len(ones) >= len(numbers) / 2 else -1) * (1 if not inverse else -1)
  return '0' if sign == -1 else '1'

def toRate(bits):
  binary = [str(bit) for bit in bits]
  return int(''.join(binary), 2)

def toRate2(numbers, inverse = False):
  position = 0

  while (len(numbers) > 1):
    positionBit = getPositionBit(numbers, position, inverse)
    numbers = [bit for bit in numbers if bit[position] == positionBit]
    position += 1
  
  return toRate(numbers[0])

with open('input', encoding="utf-8") as f:
  numbers = []

  for line in f:
    numbers += [line.replace('\n', '')]


  print(toRate2(numbers) * toRate2(numbers, True))
