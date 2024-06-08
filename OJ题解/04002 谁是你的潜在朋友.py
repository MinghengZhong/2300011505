n, m = map(int, input().split())
b = [0]*m
l = []
for i in range(n):
    a = int(input())
    l.append(a-1)
    b[a-1] += 1
for a in l:
    if b[a] == 1:
        print('BeiJu')
    else:
        print(b[a]-1)
