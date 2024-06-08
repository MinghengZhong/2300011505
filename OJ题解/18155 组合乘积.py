from sys import exit


def search(count, m, t, step, n, l):
    if step == n:
        if count == t or count*t == m:
            print('YES')
            exit()
    else:
        search(count, m, t, step+1, n, l)
        search(count*l[step], m, t, step+1, n, l)
    return


t = int(input())
l = list(map(int, input().split()))
m = 1
for a in l:
    m *= a
if m % t != 0:
    print('NO')
else:
    if t == 1:
        if t in l:
            print('YES')
        else:
            print('NO')
    else:
        search(1, m, t, 0, len(l), l)
        print('NO')
