def parse(input):
  lines = []

  for line in input:
    lines += [line.replace('\n', '')]

  return lines

openToClosingChar = { '[': ']', '(': ')', '<': '>', '{': '}' }
charScore = { ']': 2, ')': 1, '>': 4, '}': 3 }

with open('input', encoding="utf-8") as f:
  scores = [] 

  for line in parse(f):
    isCorrupted = False
    expectedClosingChars = []

    for char in line:
      isOpeningChar = char in openToClosingChar

      if (isOpeningChar):
        expectedClosingChars += openToClosingChar[char]
      else:
        closingChar = expectedClosingChars.pop()

        if char != closingChar:
          isCorrupted = True
          break

    if (not isCorrupted):
      expectedClosingChars.reverse()
      score = 0

      for char in expectedClosingChars:
        score *= 5
        score += charScore[char]

      scores += [score]

  sortedScores = sorted(scores)
  middleScore = sortedScores[round(len(scores) / 2)]

  print(middleScore)