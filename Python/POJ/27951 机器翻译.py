m, n = map(int, input().split())
l, s, ans, head = [], set(), 0, 0
for i in list(map(int, input().split())):
    if i not in s:
        ans += 1
        s.add(i)
        l.append(i)
        if len(l)-head > m:
            s.remove(l[head])
            head += 1
print(ans)
