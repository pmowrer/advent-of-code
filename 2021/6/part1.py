def parse(input):
  for line in input:
    return [int(x) for x in line.replace('\n', '').split(',')]

with open('input', encoding="utf-8") as f:
  timers = parse(f)

  for day in range(0, 80):
    nextTimers = []
    createCount = 0
    
    for timer in timers:
      if timer == 0:
        nextTimer = 6
        createCount += 1
      else:
        nextTimer = timer - 1

      nextTimers += [nextTimer]

    for c in range(0, createCount):
      nextTimers += [8]
      
    timers = nextTimers

  print(len(timers))