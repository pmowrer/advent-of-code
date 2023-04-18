from collections import defaultdict

def parse(input):
  for line in input:
    return [int(x) for x in line.replace('\n', '').split(',')]

with open('input', encoding="utf-8") as f:
  timers = defaultdict(int)

  for timer in parse(f):
    timers[timer] += 1

  for day in range(0, 256):
    newTimers = defaultdict(int)

    for k, v in timers.items():      
      k -= 1

      if k < 0:
        newTimers[6] += v
        newTimers[8] += v
      else:
        newTimers[k] += v

    timers = newTimers

  print(sum(timers.values()))
