import math

hexToBin = {
  '0': '0000',
  '1': '0001',
  '2': '0010',
  '3': '0011',
  '4': '0100',
  '5': '0101',
  '6': '0110',
  '7': '0111',
  '8': '1000',
  '9': '1001',
  'A': '1010',
  'B': '1011',
  'C': '1100',
  'D': '1101',
  'E': '1110',
  'F': '1111',
}

binToHex = {
  '0000': '0',
  '0001': '1',
  '0010': '2',
  '0011': '3',
  '0100': '4',
  '0101': '5',
  '0110': '6',
  '0111': '7',
  '1000': '8',
  '1001': '9',
  '1010': 'A',
  '1011': 'B',
  '1100': 'C',
  '1101': 'D',
  '1110': 'E',
  '1111': 'F',
}

packetToStats = {}

def parseLiteral(binStr):
  lastGroup = False
  value = ''
  v = binStr[6:]

  for i, v in enumerate(v):
    if i % 5 != 0:
      value += v
    elif v == '0':
      if lastGroup == True:
        break
  
      lastGroup = True

  print('parseLiteral', i, len(v), binStr)
  return [int(value, 2), ''.join(binStr[6 + i + 1:])]

def parseOperator(binStr):
  lengthId = binStr[6]
  packetsBinStr = ''
  numSubPackets = 0
  lenSubPackets = 0
  packets = []

  if lengthId == '0':
    lenSubPackets = int(''.join(binStr[7:22]), 2)
    packets = [binStr[22:]]
  else:
    numSubPackets = int(''.join(binStr[7:18]), 2)
    packetsBinStr = binStr[18:]
    packetMaxLength = len(packetsBinStr) / numSubPackets
    n = math.floor((packetMaxLength - 1) / 5)
    lenSubPackets = 5 * n + 1
    packets = [packetsBinStr[i:i+lenSubPackets] for i in range(0, numSubPackets * lenSubPackets, lenSubPackets)]

  return packets

def parsePacket(binStr):
  packets = [binStr]
  output = []

  while len(packets) > 0:
    packet = packets.pop(0)

    version = int(binToHex['0' + ''.join(packet[0:3])])
    typeId = binToHex['0' + ''.join(packet[3:6])]

    print('while:', packet, version, typeId, len(packets))

    if int(''.join(packet), 2) == 0:
      return output
    elif typeId == '4':
      value, remainder = parseLiteral(packet)

      print('type 4:', value, remainder, packets)

      if len(remainder) != 0 and int(remainder, 2) != 0:
        packets += [remainder]
  
      output += [[version, typeId, value]]
    else:
      packets += parseOperator(packet)
      output += [[version, typeId, 0]]    

    print('packets', packets)

  return output

def parse(input):
  binStr = []

  for line in input:
    for h in line:
      binStr += hexToBin[h]

  return ''.join(binStr)

with open('testinput1', encoding="utf-8") as f:
  binStr = parse(f)

  print(parsePacket(binStr))
    
