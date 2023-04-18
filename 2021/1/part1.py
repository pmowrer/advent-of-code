with open('input', encoding="utf-8") as f:
  largerMeasurements = 0
  lastMeasurement = 0

  measurements = [int(line) for line in f]

  for m in measurements:
    if lastMeasurement != 0 and m > lastMeasurement:
      largerMeasurements += 1

    lastMeasurement = m

  print(largerMeasurements)
