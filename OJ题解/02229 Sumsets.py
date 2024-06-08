l = [0, 1, 2, 4, 6, 10, 14]
n = int(input())//2
i = 4
while len(l) <= n+1:
    l.append((l[-1]+l[i]) % 1000000000)
    l.append((l[-1]+l[i]) % 1000000000)
    i += 1
print(l[n+1])
