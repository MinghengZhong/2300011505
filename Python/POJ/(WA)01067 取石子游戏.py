while True:
    try:
        a, b = map(int, input().split())
        if (a-b) % 2 == 0:
            print(1)
        else:
            print(0)
    except EOFError:
        break
