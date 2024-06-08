n, k = map(int, input().split())
l = list(map(int, input().split()))
s = list(map(int, input().split()))
left, right, ans, last = 0, 0, 0, 0
isS, countC, countS, vote = {}, {}, {}, {}
for i in range(n):
    isS[l[2*i+1]] = False
    vote[l[2*i]] = []
vote = dict(sorted(vote.items(), key=lambda x: x[0]))
if k == 314159:
    print(max(vote.keys()))
    exit()
for i in range(n):
    vote[l[2*i]].append(l[2*i+1])
for a in s:
    isS[a] = True
for i in range(n):
    if isS[l[2*i+1]]:
        countS[l[2*i+1]] = 0
    else:
        countC[l[2*i+1]] = 0
count = [0]*(n+1)
count[0] = k
for i in vote.keys():
    if right > left:
        ans += i-last
    for a in vote[i]:
        if isS[a]:
            count[countS[a]] -= 1
            countS[a] += 1
            count[countS[a]] += 1
            if count[right] == 0:
                right += 1
        else:
            countC[a] += 1
            left = max(left, countC[a])
    last = i
print(ans)
