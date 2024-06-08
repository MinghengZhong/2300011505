n = int(input())
l = [1, 1]
for i in range(32):
    l.append(l[-1]+l[-2])
for i in range(n):
    print(l[int(input())-1])
