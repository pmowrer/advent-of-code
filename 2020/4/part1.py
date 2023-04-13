import re

rows = open('input', 'r').read().split('\n\n')
requiredFields = re.compile('((byr|iyr|eyr|hgt|hcl|ecl|pid):[^\s\\n]*[\s\\n]*(cid:[^\s]+\s)?){7}')
validCount = 0

for row in rows:
    if requiredFields.search(row):
        validCount += 1

print(validCount)

