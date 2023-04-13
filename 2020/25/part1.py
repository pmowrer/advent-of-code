pks = open('input', 'r').read().split('\n')

# transform subject number (s)
# n as for 1 untilloop size (ls):
# v = n
# 1. v = v * ls
# 2. v = v / 20201227 remainder

sn = 7
card_pk = 5764801
# card_ls = 8

door_pk = 17807724
# card_ls = 11

# 
# 

def transform(sn, ls):
  value = 1
  i = 0

  while i < ls:
    value *= sn
    value = value % 20201227
    i += 1

  return value

def find_ls(pk):
  value = 1
  i = 0

  while True:
    if pk == value:
      return i

    value *= sn
    value = value % 20201227
    i += 1

v = 0

print(pks)

# pks = [card_pk, door_pk]

ls = [find_ls(int(pk)) for pk in pks]


print('ls', ls, transform(7, 11))

print('keys', transform(int(pks[0]), ls[1]), transform(int(pks[1]), ls[0]))