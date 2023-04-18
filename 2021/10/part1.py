def parse(input):
  lines = []

  for line in input:
    lines += [line.replace('\n', '')]

  return lines

openToClosingChar = { '[': ']', '(': ')', '<': '>', '{': '}' }

charScore = { ']': 57, ')': 3, '>': 25137, '}': 1197 }

with open('input', encoding="utf-8") as f:
  corruptedChars = []

  for line in parse(f):
    expectedClosingChars = []

    for char in line:
      isOpeningChar = char in openToClosingChar

      if (isOpeningChar):
        expectedClosingChars += openToClosingChar[char]
      else:
        closingChar = expectedClosingChars.pop()

        if char != closingChar:
          corruptedChars += char
          break

  score = 0

  for char in corruptedChars:
    score += charScore[char]

  print(score)