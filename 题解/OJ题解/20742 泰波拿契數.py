l = [0, 1, 1]
n = int(input())
if n > 2:
    for i in range(n-2):
        l.append(l[-1]+l[-2]+l[-3])
print(l[n])
