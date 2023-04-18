with open('testinput', encoding="utf-8") as f:
  largerMeasurements = 0
  lastWindowMeasurement = 0
  window = []

  measurements = [int(line) for line in f]

  for m in measurements:
    window = window[-2:] + [m]

    nextWindowMeasurement = sum(window)

    if lastWindowMeasurement > 0 and nextWindowMeasurement > lastWindowMeasurement:
      largerMeasurements += 1

    if len(window) == 3:
      lastWindowMeasurement = nextWindowMeasurement

  print(largerMeasurements)

