from functools import reduce

schedule = open('input', 'r').read().split('\n')[1].split(',')

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def findTimeStamp(schedule):
    na = [(int(busId), int(busId) - i) for i, busId in enumerate(schedule) if busId != 'x']
    print(na)
    return chinese_remainder([i[0] for i in na], [i[1] for i in na])

print(findTimeStamp(schedule))
