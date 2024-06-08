for _ in range(int(input())):
    n, q = map(int, input().split())
    l = [0]+list(map(int, input().split()))
    one, count = [], 0
    for a in l:
        if a == 1:
            count += 1
        one.append(count)
    for i in range(n):
        l[i+1] += l[i]
    for i in range(q):
        a, b = map(int, input().split())
        if b == a or l[b]-l[a-1] < one[b]-one[a-1]+b-a+1:
            print('NO')
        else:
            print('YES')
