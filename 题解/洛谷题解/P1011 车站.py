a, n, m, x = map(int, input().split())
if x == 1 or x == 2:
    print(a)
elif x == 3:
    print(2*a)
elif x == n-1:
    print(m)
elif x == n:
    print(0)
else:
    la = [0, 1, 1, 2, 2]
    lb = [0, 0, 0, 0, 1]
    for i in range(5, n):
        la.append(2*la[-1]-la[-3])
        lb.append(2*lb[-1]-lb[-3])
    b = (m-a*la[-1])//lb[-1]
    print(a*la[x]+b*lb[x])
