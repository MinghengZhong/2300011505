n = int(input())
l = list(map(int, input().split()))
t = sorted([i+1 for i in range(n)], key=lambda i: l[i-1])
ans = 0
l.sort(reverse=True)
for i in range(n):
    ans += i*l[i]
print(' '.join(map(str, t)))
print('%.2f' % (ans/n))
'''
n = int(input())
l = list(map(int, input().split()))
order = []
counted = []
ans = 0
for i in range(0, n):
    counted.append(True)
for i in range(0, n):
    small = -1
    smallorder = 0
    for j in range(0, n):
        if small == -1 and counted[j]:
            small = l[j]
            smallorder = j
        elif small != -1 and counted[j] and small > l[j]:
            small = l[j]
            smallorder = j
    counted[smallorder] = False
    order.append(smallorder+1)
    ans += l[smallorder]*(n-i-1)
for i in range(0, n-1):
    print(order[i], end=' ')
print(order[n-1])
print(format(ans/n, '.2f'))
'''
