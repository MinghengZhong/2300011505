n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in l:
    ans += i
print(ans/n)
