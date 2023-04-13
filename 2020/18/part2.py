rows = open('input', 'r').read().split('\n')

def findClosingBracketIndex(str):
  open = 1
  i = 1

  while open > 0 and i < len(str) - 1:
    i += 1

    if str[i] == '(':
      open += 1
    elif str[i] == ')':
      open -= 1
    
  return i

def calculate(expression):
  total = 0
  x = ''
  skipTill = 0

  open = 0

  for i, c in enumerate(expression):
    if i >= skipTill:
      if c.isnumeric() is True:
        if x == '' or x == '+':
          total += int(c)
        elif x == '*':
          total *= int(c)
      elif c == '*' or c == '+':
        x = c
      elif c == '(':
        g = findClosingBracketIndex(expression[i + 1:])
        b = calculate(expression[(i + 1):i + g + 2])
        print('bracket',expression[(i + 1):i + g + 2], b )

        if x == '' or x == '+':
          total += b
        elif x == '*':
          total *= b

        skipTill = b
      
  return total

# import re
 
# parseRule = re.compile('((?:\d \+ )+(?:\d|(\([\d\*\+ ]+\))))+')

# def test(expression):
#   g = parseRule.search(expression).groups()

#   print('groups', g)

#   return expression

# break string into operations
# 2 * 3 + (4 * 5)
# => 0: 2 * 
# => 1: 3 +

# 5: o=1 i=0
# 8*: o=2 
# 3: o=3
# 9: o=4
# 3: o=2 (close all until *)
# 4: o=2
# 3: o=0 (* closes, close rest)

# 2: (001)
# 4: (00)
# 9: (0)
# 6: (001)
# 9: (00)
# 8: (001)
# 6: (0)

#  (((((2 + 4) * 9) * (((6 + 9) * (8 + 6)) + 6))) + (2 + 4) * 2
# (11000 + (2 + 4) * 2
#

def test(expression):
  newExpression = ''
  close = -1
  open = []

  for i, c in enumerate(expression):
    if c == '':
      continue

    #print(i, c, i < len(expression) - 2)
    if c.isnumeric() is True:
      if i < len(expression) - 2 and expression[i + 1] != ')':
        if expression[i + 2] == '+':
          newExpression += '('
          open.append(1)
        else:
          close = True

    elif c == '(':
      open.append(1)
      newExpression += '('
      open.append(0)

    newExpression += c

    if c == ')':
      j = open.pop()

      while (len(open) > 0 and j != 0):
        j = open.pop()
        newExpression += ')'
  
    if close == True:
      j = len(open) - 1

      while (j > 0 and open[j] == 1):
        j = open.pop()
        newExpression += ')'
        j = len(open) - 1

      close = False

 
  print('newExpression', newExpression)

  return newExpression

print(test('1 + (2 * 3) + (4 * (5 + 6))'))
print(test('2 * 3 + (4 * 5)'))
print(calculate(test('5 + (8 * 3 + 9 + 3 * 4 * 3)')))
print(calculate(test('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')))

total = 0

#for row in rows:
#  total += calculate(row)
#
#print(total)