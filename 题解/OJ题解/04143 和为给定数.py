n = int(input())
a, b = set(), set()
for x in map(int, input().split()):
    if x in a:
        b.add(x)
    else:
        a.add(x)
m = int(input())
ans = m+1
for x in a:
    if x < ans:
        if x+x == m:
            if x in b:
                ans = x
        elif m-x in a:
            ans = x
if ans == m+1:
    print('No')
else:
    print(ans, m-ans)
