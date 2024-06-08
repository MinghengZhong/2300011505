n = int(input())
nums = list(map(int, input().split()))
N = max(nums)
l = [0]*(N+1)
for i in nums:
    l[i] += 1
dp = [0, l[1]]
for i in range(2, N+1):
    dp.append(max(dp[i-1], dp[i-2]+l[i]*i))
print(dp[-1])
