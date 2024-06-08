import sys


def F(x):
    if x > 0:
        return -x
    else:
        return int((-x)**.5+1)**2


input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
l, g = [], [0.5]*m
for _ in num_list:
    i0 = _ % m
    i = i0
    j = 1
    while g[i] != 0.5 and g[i] != _:
        i = (i0+j) % m
        j = F(j)
    g[i] = _
    l.append(i)
print(*l)
