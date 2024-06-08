while True:
    try:
        a, b = input().split()
        i = 0
        for j in b:
            if j == a[i]:
                i += 1
                if i == len(a):
                    break
        print('Yes' if i == len(a) else 'No')
    except EOFError:
        break
