n = int(input())
s = []
ans = [0]*n
for i, a in enumerate(map(int, input().split())):
    while s and s[-1][0] < a:
        ans[s.pop()[1]] = i+1
    s.append((a, i))
print(*ans)
