n = int(input())
pre = '00'
ans = 0
for i in range(0, n):
    s = input()
    if s != pre:
        ans += 1
        pre = s
print(ans)
