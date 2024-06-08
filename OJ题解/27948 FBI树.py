def suf(s, n):
    if s == '1':
        print('I', end='')
        return 'I'
    if s == '0':
        print('B', end='')
        return 'B'
    a, b = suf(s[0:1 << (n-1)], n-1), suf(s[1 << (n-1):], n-1)
    if a == b:
        print(a, end='')
        return a
    else:
        print('F', end='')
        return 'F'


n = int(input())
s = input()
k = suf(s, n)
