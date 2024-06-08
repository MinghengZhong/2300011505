def search(n, i, j):
    global right
    if j-i == 1:
        return j
    k = (i+j)//2
    if right[k] <= n+1:
        return search(n, k, j)
    else:
        return search(n, i, k)


n = int(input())
l = list(map(int, input().split()))
suml = sum(l)
if suml % 3 != 0:
    print(0)
else:
    suml = suml//3
    count = 0
    left = []
    right = []
    for i in range(n):
        count += l[i]
        if count == suml:
            left.append(i)
        if count == 2*suml and i != n-1:
            right.append(i+1)
    ans = 0
    last = 0
    for a in left:
        if a >= right[-1]-1:
            break
        elif a <= right[last]-2:
            ans += len(right)-last
        else:
            last = search(a, last, len(right)-1)
            ans += len(right)-last
    print(ans)
