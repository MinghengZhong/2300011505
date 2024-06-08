s = input().split()
h = int(s[1])
l = list(map(int, input().split()))
ans = 0
for i in l:
    if i > h:
        ans += 2
    else:
        ans += 1
print(ans)
