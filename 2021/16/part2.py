from dataclasses import dataclass
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

@dataclass
class Packet:
  version: int
  type_id: str
  packets: list
  value: int

def parse_input(input):
  packet = []

  for line in input:
    for h in line:
      packet += hexToBin[h]

  return ''.join(packet)

def parse_packet_header(bin_str):
  return [int(binToHex['0' + ''.join(bin_str[0:3])]),  binToHex['0' + ''.join(bin_str[3:6])]]

def parse_packet_value(bin_str):
  last_group = False
  value = ''
  v = bin_str[6:]

  for i, v in enumerate(v):
    if i % 5 != 0:
      value += v
    elif v == '0':
      if last_group == True:
        break
  
      last_group = True

  return int(value, 2)
  #return [int(value, 2), ''.join(packet[6 + i + 1:])]

def parse_packet_operator(bin_str):
  length_type_id = bin_str[6]
  packets_bin_str = ''
  num_sub_packets = 0
  len_sub_packets = 0
  bin_strs = []

  if length_type_id == '0':
    len_sub_packets = int(''.join(bin_str[7:22]), 2)
    bin_strs = [bin_str[22:]]
  else:
    num_sub_packets = int(''.join(bin_str[7:18]), 2)
    packets_bin_str = bin_str[18:]
    packets_max_length = len(packets_bin_str) / num_sub_packets
    n = math.floor((packets_max_length - 1) / 5)
    len_sub_packets = 5 * n + 1
    bin_strs = [packets_bin_str[i:i+len_sub_packets] for i in range(0, num_sub_packets * len_sub_packets, len_sub_packets)]

  print(len_sub_packets, bin_strs)

  return bin_strs
  
# build packet graph
# recursively: pass parent
# parse the packet version and type
# if packet is an operator, apply recursive function to each sub-packet
# if packet is a value, return value
def build_packet_graph(bin_str, parent = None):
  version, type_id = parse_packet_header(bin_str)
 
  value = parse_packet_value(bin_str) if type_id == '4' else None

  packet = Packet(version, type_id, [], value)

  print(packet, value)

  if parent != None:
    parent.packets += [packet]

  if type_id != '4':
    packets = parse_packet_operator(bin_str)
    
    for p in packets:
      build_packet_graph(p, packet)
  
  return packet

with open('testinput2', encoding="utf-8") as f:
  packet = parse_input(f)

  print(build_packet_graph(packet))
    
