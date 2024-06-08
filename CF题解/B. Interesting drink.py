def search(n, i, j):
    global l
    if j-i <= 1:
        return i
    else:
        k = (i+j)//2
        if l[k] <= n:
            return search(n, k, j)
        else:
            return search(n, i, k)


n = int(input())
l = sorted([0]+list(map(int, input().split())))
q = int(input())
for i in range(q):
    m = int(input())
    if m >= l[-1]:
        print(n)
    elif m < l[1]:
        print(0)
    else:
        print(search(m, 0, n))
