t = int(input())
n = []
ans = [0, 1]
for _ in range(t):
    n += [int(input())]
for i in range(1, max(n)):
    ans += [(ans[-1]*2+ans[-2]) % 32767]
for nn in n:
    print(ans[nn])
