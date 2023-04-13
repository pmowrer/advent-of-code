input = open('input', 'r').read().split('\n')
rowLength = len(input[0])

def ski(x, y):
  i = x;
  j = y;
  trees = 0;

  while j < len(input):
    if input[j][i] == '#':
      trees += 1

    i = (i + x) % (rowLength)
    j += y

  return trees

multipliedTrees = ski(1, 1) * ski(3, 1) * ski(5, 1) * ski(7, 1) * ski(1, 2)

print(multipliedTrees)