while True:
    s = float(input())
    if s == 0:
        break
    else:
        n = 1
        while True:
            s -= 1/(n+1)
            if s <= 0:
                print(str(n)+' card(s)')
                break
            else:
                n += 1
