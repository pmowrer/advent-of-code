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
  
  return False if index in seen else acc

result = False
index = 0

while result is False:
  instruction = instructions[index].split(' ')
  operation = instruction[0]

  if operation in ['nop', 'jmp']:
    newInstructions = instructions[:]
    newInstructions[index] = ('jmp' if operation == 'nop' else 'nop') + ' ' + instruction[1]
    result = runProgram(newInstructions)

  index += 1   

print(result)