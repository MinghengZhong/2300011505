import numpy as np
from math import sinh, cosh, pow
import matplotlib.pyplot as plt


def p(x, nc, ns):
    return pow(cosh(x[0]+x[1]), nc)*pow(sinh(x[0]+x[1]), ns)


def n(x, nc, ns):
    return pow(cosh(-x[0]+x[1]), nc)*pow(sinh(-x[0]+x[1]), ns)


def F(a, b):
    x = (a, b)
    return p(x, 3, 1)+n(x, 3, 1)-p(x, 4, 0)+n(x, 4, 0)


a = 2.8854
a = 1/a
x = np.linspace(-0.05, 0.05, 1000)
y = [F(a, b) for b in x]
plt.plot(x, y)
plt.axhline(0)
plt.show()
for i in range(len(x)-1):
    if y[i]*y[i+1] <= 0:
        print(x[i])
