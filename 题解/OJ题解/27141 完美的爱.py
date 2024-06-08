n = int(input())
l = [0]+list(map(int, input().split()))
dic = {0: 0}
for i in range(1, n+1):
    l[i] += l[i-1]-520
    dic[l[i]] = i
ans = 0
for i in range(n+1):
    ans = max(ans, dic[l[i]]-i)
print(ans*520)
