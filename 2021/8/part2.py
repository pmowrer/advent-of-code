from collections import defaultdict

def parse(input):
  entries = []

  for line in input:
    entries += [[x.split(' ') for x in line.replace('\n', '').split(' | ')]]

  return entries

def findCommon(list1, list2):
  return list(set(list1).intersection(list2))

def orderByMostCommonWith(list, comparison):
  return sorted(list, key=lambda x: len(findCommon(x, comparison)), reverse=True)  

def orderByLeastCommonWith(list, comparison):
  return sorted(list, key=lambda x: len(findCommon(x, comparison)))  

def findDifference(list1, list2):
  return list(set(list1) ^ set(list2))

def sort(str):
  return ''.join(sorted(str))

def deduceDigits(signalValues):
  # map of signal values by their length
  valuesByLength = {}
  # map of segments to the signal values that contain them
  segmentToValues = {}
  # map of the number of values per segment to values
  valuesCountToValues = defaultdict(int)
  # copy of signalValues with each value sorted TODO: handle during parsing
  sortedValues = []
  # the final product - map of signal values to the corresponding digit
  valuesToDigit = {}
  
  for value in signalValues:
    valueLength = len(value)
    sortedValue = sort(value)
    sortedValues += [sortedValue]

    for segment in sortedValue:
      segmentToValues.setdefault(segment, [])
      segmentToValues[segment] += [sortedValue]

    digit = None

    if valueLength == 2:
      digit = 1
    elif valueLength == 3:
      digit = 7
    elif valueLength == 4:
      digit = 4
    elif valueLength == 7:
      digit = 8

    if digit:
      valuesToDigit[sortedValue] = digit

    valuesByLength.setdefault(valueLength, [])
    valuesByLength[valueLength] += [sortedValue]

  for segment, values in segmentToValues.items():
    numValues = len(values)
    valuesCountToValues[numValues] = values
  
  # all digits but 2 (nine total) share the "f" segment
  two = ''.join(findDifference(sortedValues, valuesCountToValues[9]))
  
  # 3 and 5 have the same number of segments as 2. 3 has four in common with 2, while 5 has three.
  two, three, five = orderByMostCommonWith(valuesByLength[5], two)

  # we can deduce which of the length six digits is 9 based on their segment similarity to 3.
  nine = orderByMostCommonWith(valuesByLength[6], three)[0]
  # similarly find six 6 based on asymmetry with 7
  six = orderByLeastCommonWith(valuesByLength[6], valuesByLength[3][0])[0]
  # and finally by method of exclusion
  zero = findDifference(valuesByLength[6], [six, nine])[0]

  valuesToDigit[zero] = 0
  valuesToDigit[two] = 2
  valuesToDigit[three] = 3
  valuesToDigit[five] = 5
  valuesToDigit[six] = 6
  valuesToDigit[nine] = 9

  return valuesToDigit

with open('input', encoding="utf-8") as f:
  entries = parse(f)
  values = []

  for entry in entries:   
    value = ''
    valuesToDigit = deduceDigits(entry[0])

    for outputValue in entry[1]:
      sortedOutputValue = sort(outputValue)

      if (sortedOutputValue in valuesToDigit):
        value += str(valuesToDigit[sort(outputValue)])

    values += [int(value)]

  print(sum(values))