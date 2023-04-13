input = [15,5,1,4,7,0]

queue = input
queue.reverse()
seen = {}
turn = 0

while (turn < 30000000):
  last = queue.pop()

  if len(queue) == 0:
    if last not in seen:
      queue.append(0)
    else:
      queue.append(turn - seen[last])

  seen[last] = turn
  turn += 1

print(last)