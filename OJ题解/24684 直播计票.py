from collections import defaultdict
dic = defaultdict(int)
l = list(map(int, input().split()))
for n in l:
    dic[n] += 1
maxn = max(dic.values())
ans = []
for a in dic.items():
    if a[1] == maxn:
        ans.append(a[0])
ans.sort()
print(' '.join(list(map(str, ans))))
