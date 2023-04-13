rows = open('input', 'r').read().split('\n\n')
count = 0

for row in rows:
    count += len(set(row.replace('\n', '')))

print(count)
