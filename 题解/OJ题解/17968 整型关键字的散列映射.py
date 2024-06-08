import sys
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
    i = _ % m
    while g[i] != 0.5 and g[i] != _:
        i = (i+1) % m
    g[i] = _
    l.append(i)
print(*l)
