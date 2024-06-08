n = int(input())
ans = 0
count = 0
while n > 0:
    n -= 1
    s = input().split()
    count = count-int(s[0])+int(s[1])
    ans = max(ans, count)
print(ans)
