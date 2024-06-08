t = int(input())
ans = []
for _ in range(t):
    n, x = map(int, input().split())
    l = [0]+list(map(int, input().split()))+[x]
    for i in range(n+1):
        l[i] = l[i+1]-l[i]
    l.pop()
    l[-1] *= 2
    ans += [max(l)]
for a in ans:
    print(a)
