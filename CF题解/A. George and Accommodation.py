n = int(input())
ans = 0
for i in range(0, n):
    s = input().split()
    if int(s[1])-int(s[0]) >= 2:
        ans += 1
print(ans)
