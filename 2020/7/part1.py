import re

parseRule = re.compile('^(\w+ \w+)(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?(?:[^0-9]*([0-9] \w+ \w+))?')

rules = open('input', 'r').read().split('\n')
bags = {}

for rule in rules:
  parsed = parseRule.match(rule).groups()
  bag = parsed[0]
  contents = parsed[1:]

  for content in contents:
    if content != None:
      color = content[2:]
      bags[color] = (bags[color] if color in bags else []) + [bag]
 
queue = bags['shiny gold']
seen = {}
count = 0

while len(queue) > 0:
  next = queue.pop()

  if not next in seen:
    count += 1
    seen[next] = next

    if next in bags:
      queue += bags[next]

print(count)

