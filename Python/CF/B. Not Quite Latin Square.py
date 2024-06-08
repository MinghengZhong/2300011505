for _ in range(int(input())):
    s = input()+input()+input()
    d = {'A': 0, 'B': 0, 'C': 0, '?': 0}
    for a in s:
        d[a] += 1
    for a in d.items():
        if a[1] == 2:
            print(a[0])
            break
