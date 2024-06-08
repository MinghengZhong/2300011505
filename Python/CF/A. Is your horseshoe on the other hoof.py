a = list(map(int, input().split()))
b = []
ans = 0
for i in a:
    if i in b:
        ans += 1
    else:
        b.append(i)
print(ans)
