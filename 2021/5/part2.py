def parse(input):
  lines = []

  for line in input:
    line = line.replace('\n', '').replace(' -> ', ',')
    x1, y1, x2, y2 = line.split(',') 
    lines += [[[x1, y1], [x2, y2]]]
        
  return lines

with open('input', encoding="utf-8") as f:
  lines = parse(f)
  points = {}
  overlapping = 0

  for p1, p2 in lines:
    x1, y1 = p1
    x2, y2 = p2

    if y1 == y2:
      sign = -1 if int(x2) < int(x1) else 1
      lineNumbers = range(int(x1), int(x2) + sign, sign)

      for i in lineNumbers:
        point = f'{i},{y1}'

        points.setdefault(point, 0)
        points[point] += 1

        if points[point] == 2:
          overlapping += 1

    elif x1 == x2:
      sign =  -1 if int(y1) > int(y2) else 1
      lineNumbers = range(int(y1), int(y2) + sign, sign)

      for i in lineNumbers:
        point = f'{x1},{i}'

        points.setdefault(point, 0)
        points[point] += 1

        if points[point] == 2:
          overlapping += 1

    else:
      if abs(int(x1) - int(x2)) == abs(int(y1) - int(y2)):
        signX = -1 if int(x2) < int(x1) else 1
        signY = -1 if int(y1) > int(y2) else 1
        newY = int(y1)

        lineNumbers = range(int(x1), int(x2) + signX, signX)

        for i in lineNumbers:
          point = f'{i},{newY}'
          newY += signY

          points.setdefault(point, 0)
          points[point] += 1

          if points[point] == 2:
            overlapping += 1

  print(overlapping)


