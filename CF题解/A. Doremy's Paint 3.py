N = int(input())
for _ in range(N):
    n = int(input())
    l = input().split()
    ll = []
    count = 0
    for a in l:
        if a not in ll:
            ll.append(a)
        else:
            if ll[0] == a:
                count += 1
            else:
                count -= 1
        if len(ll) == 3:
            break
    if len(ll) == 3:
        print('No')
    elif len(ll) == 1:
        print('Yes')
    elif len(ll) == 2:
        if count == 1 or count == 0 or count == -1:
            print('Yes')
        else:
            print('No')
