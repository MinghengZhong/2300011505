n = int(input())
l = list(map(int, input().split()))
l.sort()
print(l[0], end='')
for i in range(1, len(l)):
    print(' '+str(l[i]), end='')
