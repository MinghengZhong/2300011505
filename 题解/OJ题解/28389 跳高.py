from bisect import bisect_left as b
n = input()
q = []
for x in list(map(int, input().split()))[::-1]:
    i = b(q, x)
    if i-len(q):
        q[i] = x
    else:
        q.append(x)
print(len(q))
