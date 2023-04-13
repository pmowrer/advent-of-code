rows = open('input', 'r').read().split('\n\n')
count = 0

for row in rows:
    persons = row.split('\n')
    allUniqueAnswers = set(row.replace('\n', ''))    
    count += len(allUniqueAnswers.intersection(*persons))

print(count)
