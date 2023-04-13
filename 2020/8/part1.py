instructions = open('input', 'r').read().split('\n')

def runProgram(input):
  acc = 0
  seen = {}
  index = 0

  while not index in seen and index < len(input):
    instruction = input[index].split(' ')
    seen[index] = index
    n = int(instruction[1][1:])

    if instruction[1][0] == '-':
      n *= -1

    if instruction[0] == 'acc':
      acc += n
      index += 1
    elif instruction[0] == 'jmp':
      index += n
    else:
      index += 1
  
  return acc

print(runProgram(instructions))