from math import gcd


class fraction:
    def __init__(self, a, b):
        g = gcd(a, b)
        if a*b >= 0:
            self.top = abs(a)//g
            self.bottom = abs(b)//g
        else:
            self.top = -abs(a)//g
            self.bottom = abs(b)//g

    def __str__(self):
        return '%d/%d' % (self.top, self.bottom)

    def __add__(self, other):
        e = self.top*other.bottom+self.bottom*other.top
        f = self.bottom*other.bottom
        return fraction(e, f)


a, b, c, d = map(int, input().split())
print(fraction(a, b)+fraction(c, d))

'''
a, b, c, d = map(int, input().split())
e, f = a*d+b*c, b*d
if e*f < 0:
    print('-', end='')
g = gcd(e, f)
print('%d/%d' % (abs(e)//g, abs(f)//g))
'''
