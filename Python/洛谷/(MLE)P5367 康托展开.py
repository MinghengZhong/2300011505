n = int(input())
l = tuple(map(int, input().split()))
factorial = [1]*(n+1)
for i in range(1, n+1):
    factorial[i] = (factorial[i-1]*i) % 998244353
ans = 1
num = [1]*n
for i in range(0, n-1):
    num[l[i]-1] = 0
    ans = (ans+sum(num[:l[i]-1])*factorial[n-i-1]) % 998244353
print(ans)
