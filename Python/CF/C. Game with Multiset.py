m = int(input())
ans, l = [], [0]*32


for _ in range(m):
    o, n = map(int, input().split())
    if o == 1:
        l[n] += 1
        continue
    count = 0
    for i in range(31):
        if n % (2 << i) > (l[i]+count)*(1 << i):
            ans.append(False)
            break
        count = (l[i]+count-(n % (2 << i))//(1 << i))//2
        n -= n % (2 << i)
        if n == 0:
            ans.append(True)
            break
print('\n'.join(['YES' if a else 'NO' for a in ans]))
