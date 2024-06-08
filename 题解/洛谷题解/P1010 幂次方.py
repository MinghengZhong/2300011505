import math


def two(head, n):
    if head:
        plus = ''
        head = False
    else:
        plus = '+'
    if n == 0:
        return ''
    elif n == 1:
        return plus+'2(0)'
    elif n == 2:
        return plus+'2'
    elif n == 3:
        return plus+'2+2(0)'
    else:
        return plus+'2('+two(True, int(math.log(n, 2)))+')'+two(False, n-2**int(math.log(n, 2)))


print(two(True, int(input())))
