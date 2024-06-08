n = int(input())
l = list(map(int, input().split()))
ans, fact, num = 1, 1, [0]*n
num[l[-1]-1] = 1
for i in range(1, n):
    fact *= i
    ans += sum(num[:l[-i-1]])*fact
    num[l[-i-1]-1] = 1
print(ans % 998244353)
