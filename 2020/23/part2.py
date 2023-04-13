rows = open('input', 'r').read().split('\n')

class Node: 
  def __init__(self, label): 
    self.label = label 
    self.next = None

class LinkedList: 
  def __init__(self):  
      self.head = None
  
  def print(self):
    s = ''
    node = self.head

    while node != None:
      s += str(node.label)
      node = node.next

      if node == self.head:
        break
    
    return s

labelToCup = {}
cups = LinkedList()
curr = None
n = 0

for x in ([int(x) for x in '872495136'] + list(range(10, pow(10, 6) + 1))):
  n += 1
  node = Node(x)
  labelToCup[x] = node

  if curr == None:
    cups.head = node
  else:
    curr.next = node

  curr = node

curr.next = cups.head
curr = cups.head
move = 0
moves = pow(10, 7)

while move < moves:
  d = ((curr.label - 1) % n)
  d = n if d == 0 else d

  ps = curr.next
  p = None
  pickup = []
  i = 0

  while i < 3:
    p = p.next if p != None else ps
    pickup.append(p.label)
    i += 1

  while d in pickup:
    d = ((d - 1) % n) if d > 1 else n

  dest = labelToCup[d]

  curr.next = p.next
  p.next = dest.next
  dest.next = ps

  move += 1
  curr = curr.next

cups.head = labelToCup[1]

print(cups.head.next.label * cups.head.next.next.label)