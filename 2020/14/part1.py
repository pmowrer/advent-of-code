rows = open('input', 'r').read().split('\n')
mask = ''
mem = {}

for row in rows:
  command = row.split(' = ')

  if command[0] == 'mask':
    mask = command[1]
  elif command[0][0:3] == 'mem':
    address = command[0][3:].replace('[', '').replace(']', '')
    value = bin(int(command[1]))[2:].rjust(36, '0')
    masked = ''.join([value[i] if x == 'X' else ('1' if x == '1' else '0') for i, x in enumerate(mask)])
    mem[address] = masked

print(sum([int(x, 2) for x in mem.values()]))
