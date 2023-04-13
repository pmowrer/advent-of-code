rows = open('input', 'r').read().split('\n')

def calculate(expression):
  total = 0
  x = ''
  skipTill = 0

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
        open = 1
        j = i + 1

        while open > 0:
          if expression[j] == '(':
            open += 1
          elif expression[j] == ')':
            open -= 1

          j += 1

        b = calculate(expression[(i + 1):j - 1])

        if x == '' or x == '+':
          total += b
        elif x == '*':
          total *= b

        skipTill = j
      
  return total

#print(calculate('2 * 3 + (4 * 5)'))
#print(calculate('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
#print(calculate('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
#print(calculate('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))

total = 0

for row in rows:
  total += calculate(row)

print(total)