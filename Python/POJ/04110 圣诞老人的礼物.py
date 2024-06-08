n, W = map(int, input().split())
ans, v, w = 0, [], []
for i in range(n):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)
l = sorted([i for i in range(n)], key=lambda x: -v[x]/w[x])
for i in l:
    if W >= w[i]:
        W -= w[i]
        ans += v[i]
    else:
        ans += v[i]*W/w[i]
        break
print('%.1f' % (ans))

'''
v = []
w = []


def compare(i, j):
    global v, w
    if v[i]/w[i] > v[j]/w[j]:
        return 1
    elif v[i]/w[i] == v[j]/w[j]:
        return 0
    else:
        return -1


def Sort(l):
    if len(l) <= 1:
        return l
    else:
        i = l[len(l)//2]
        return Sort([j for j in l if compare(i, j) == -1])+[j for j in l if compare(i, j) == 0]+Sort([j for j in l if compare(i, j) == 1])


n, W = map(int, input().split())
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    v.append(a)
    w.append(b)
l = Sort([i for i in range(n)])
for i in l:
    if W >= w[i]:
        W -= w[i]
        ans += v[i]
    else:
        ans += v[i]*W/w[i]
        break
print('%.1f' % (ans))
'''
