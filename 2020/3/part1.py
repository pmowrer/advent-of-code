input = open('input', 'r').read().split('\n')
trees = 0;
x = 3;
y = 1;
rowLength = len(input[0])

while y < len(input):
  if input[y][x] == '#':
    trees += 1

  x = (x + 3) % (rowLength)
  y += 1

print(trees)