def parse(input):
  heightMap = []

  for line in input:
    heightMap += [[int(x) for x in line.replace('\n', '')]]

  return heightMap

with open('input', encoding="utf-8") as f:
  heightMap = parse(f)
  riskLevelSum = 0
  
  for i in range(0, len(heightMap)):
    for j in range(0, len(heightMap[i])):
      height = heightMap[i][j]

      up = j - 1
      down = j + 1
      left = i - 1
      right = i + 1

      isLowerUp = up < 0 or heightMap[i][up] > height
      isLowerDown = down >= len(heightMap[i]) or heightMap[i][down] > height
      isLowerLeft = left < 0 or heightMap[left][j] > height
      isLowerRight = right >= len(heightMap) or heightMap[right][j] > height

      if (isLowerUp and isLowerDown and isLowerLeft and isLowerRight):
        riskLevelSum += height + 1

  print(riskLevelSum)

