n = int(input())
l = list(map(int, input().split()))
count = [0]*100001
num = [0]*100001
ans = 0
maxn = 0
for i in range(n):
    count[num[l[i]]] -= 1
    num[l[i]] += 1
    count[num[l[i]]] += 1
    maxn = max(maxn, num[l[i]])
    if count[0] == -1 or maxn == 1 or (count[maxn] == 1 and count[maxn-1]+count[maxn]+count[0] == 0) or (count[1] == 1 and count[maxn]+count[1]+count[0] == 0):
        ans = i
print(ans+1)
