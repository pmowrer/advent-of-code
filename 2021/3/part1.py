def toRate(bits):
  binary = [str(bit) for bit in bits]
  return int(''.join(binary), 2)

with open('input', encoding="utf-8") as f:
  frequency = []

  for line in f:
    bits = [int(bit) for bit in line.replace('\n', '')]
    frequency = [0 if len(frequency) == 0 else frequency[i] + (1 if bit > 0 else -1) for i, bit in enumerate(bits)]

gamma = [1 if bit > 0 else 0 for bit in frequency]
epsilon = [1 if bit < 0 else 0 for bit in frequency]

print(toRate(gamma) *  toRate(epsilon))

