l = []
n = int(input())
for _ in range(n):
    l.append(set(input().split()[1:]))
for _ in range(int(input())):
    a = []
    s = input()
    for i in range(n):
        if s in l[i]:
            a.append(i+1)
    print(' '.join(map(str, a)) if a else 'NOT FOUND')
