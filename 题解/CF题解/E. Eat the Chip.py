for _ in range(int(input())):
    h, w, xa, ya, xb, yb = map(int, input().split())
    if xb <= xa:
        print('Draw')
    elif (xb-xa) % 2 == 1:
        step = (xb-xa)//2+1
        if abs(yb-ya) <= 1:
            print('Alice')
        elif ya < yb:
            if step >= w-ya:
                print('Alice')
            else:
                print('Draw')
        else:
            if step >= ya-1:
                print('Alice')
            else:
                print('Draw')
    else:
        step = (xb-xa)//2
        if ya == yb:
            print('Bob')
        elif ya < yb:
            if step >= yb-1:
                print('Bob')
            else:
                print('Draw')
        else:
            if step >= w-yb:
                print('Bob')
            else:
                print('Draw')
