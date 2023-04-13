import re

rows = open('input', 'r').read().split('\n\n')
print('rows', len(rows));

requiredFields = re.compile('((byr:(19[2-9][0-9]|200[0-2])|(iyr:(201[0-9]|2020))|(eyr:(202[0-9]|2030))|(hgt:((1(([5-8][0-9])|(9[0-3]))cm)|((59|6[0-9]|7[0-6])in)))|(hcl:#[0-9a-f]{6})|(ecl:(amb|blu|brn|gry|grn|hzl|oth))|(pid:[0-9]{9}))([\s\\n]|$)+(cid:[^\s]+\s?)?){7}')
validCount = 0

for row in rows:
    if requiredFields.search(row):
        validCount += 1
        print(row.replace('\n', '\\n'))
print(validCount)

