with open('input', encoding="utf-8") as f:
  position = 0
  depth = 0
  aim = 0

  for line in f:
    command, value = line.split(' ')

    if command == 'forward':
      position += int(value)
      depth += aim * int(value)
    elif command == 'up':
      aim -= int(value)
    elif command == 'down':
      aim += int(value)

print([position, depth, aim, position * depth])