with open('input', encoding="utf-8") as f:
  position = 0
  depth = 0

  for line in f:
    command, value = line.split(' ')

    if command == 'forward':
      position += int(value)
    elif command == 'up':
      depth -= int(value)
    elif command == 'down':
      depth += int(value)

print([position, depth, position * depth])