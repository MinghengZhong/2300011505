while True:
    try:
        s = input()
    except EOFError:
        break
    print('YES' if s[::-1] == s else 'NO')
