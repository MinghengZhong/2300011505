from collections import defaultdict
n, x, y = map(int, input().split())
l, d = defaultdict(int), defaultdict(int)
for _ in range(n):
    s = input().split()
    l[s[1]] += 1
    d[s[1]] += int(s[2])
for _ in range(int(input())):
    s = input()
    if l[s] >= x and d[s]/l[s] > y:
        print('yes')
    else:
        print('no')
