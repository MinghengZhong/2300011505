x, y, m, n, l = map(int, input().split())
if x == y:
    print(0)
elif m % l == n % l:
    print(0)
else:
    m %= l
    n %= l
    x = y-x
    m = m-n
    if x < 0:
        x += l
    if m < 0:
        m += l
    if x % m == 0:
        print(int(x/m))
    else:
        if l % m == 0:
            print('Impossible')
        else:
            a = [x % m]
            i = 1
            while True:
                if (x % m+i*(l % m)) % m == 0:
                    print(int((x+i*l)/m))
                    break
                elif x % m+i*(l % m) in a:
                    print('Impossible')
                    break
                else:
                    a.append(x % m+i*(l % m))
                    i += 1
