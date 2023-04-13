input = open('input', 'r').read().split('\n')
validCount = 0;

for str in input:
  parts = str.split(' ')
  positions = parts[0].split('-')
  index1 = int(positions[0]) - 1
  index2 = int(positions[1]) - 1
  char = parts[1][0]
  password = parts[2]

  if password[index1] != password[index2] and (password[index1] == char or password[index2] == char):
    validCount += 1

print(validCount)