def newl(l, new):
    i = 0
    j = len(l)-1
    while True:
        if l[i] <= new:
            k = i
            break
        elif l[j] >= new:
            k = j+1
            break
        elif j-i == 1:
            k = j
            break
        else:
            k = (i+j)//2
            if l[k] < new:
                j = k
            elif l[k] > new:
                i = k
            else:
                break
    l.insert(k, new)
    return l


n = int(input())
l = list(map(int, input().split()))
l.sort(reverse=True)
if n == 1:
    print(l[0])
else:
    ans = 0
    for i in range(n-2):
        new = l.pop()+l.pop()
        ans += new
        l = newl(l, new)
    print(ans+l[0]+l[1])
