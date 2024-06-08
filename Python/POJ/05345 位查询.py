n, m = map(int, input().split())
l = list(map(int, input().split()))
d = 0
for _ in range(m):
    s, i = input().split()
    if s == 'C':
        d += int(i)
    else:
        print(sum(((a+d) >> int(i)) % 2 for a in l))
