rows = open('input', 'r').read().split('\n')
mask = ''
mem = {}

for row in rows:
  command = row.split(' = ')

  if command[0] == 'mask':
    mask = command[1]
  elif command[0][0:3] == 'mem':
    value = int(command[1])
    addresses = [bin(int(command[0][3:].replace('[', '').replace(']', '')))[2:].rjust(36, '0')]

    for i, x in enumerate(mask):
      if x == 'X':
        newAddresses = []
        for address in addresses:
          newAddresses.append(address[0:i] + ('1' if address[i] == '0' else '0') + address[i+1:])
        addresses += newAddresses
      elif x == '1':
        for j, address in enumerate(addresses):
          addresses[j] = address[0:i] + '1' + address[i+1:]

    for address in addresses:
      mem[int(address, 2)] = value

print(sum(mem.values()))
