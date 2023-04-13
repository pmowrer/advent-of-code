input = open('input', 'r').read().split('\n')
validCount = 0;

for str in input:
  parts = str.split(' ')
  range = parts[0].split('-')
  min = int(range[0])
  max = int(range[1])
  char = parts[1][0]
  password = parts[2]
  charCount = 0
  index = 0

  while index < len(password):
    if password[index] == char:
      charCount += 1

    index += 1

  if charCount >= min and charCount <= max:
    validCount += 1

print(validCount)