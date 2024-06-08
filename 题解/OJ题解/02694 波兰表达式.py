s = []


def next(m):
    global s
    count = 1
    for i in range(m+1, len(s)):
        if count == 0:
            return i
        if s[i] == '+' or s[i] == '-' or s[i] == '*' or s[i] == '/':
            count += 1
        else:
            count -= 1


def poland(n):
    global s
    if s[n] == '+':
        return poland(n+1)+poland(next(n))
    elif s[n] == '-':
        return poland(n+1)-poland(next(n))
    elif s[n] == '*':
        return poland(n+1)*poland(next(n))
    elif s[n] == '/':
        return poland(n+1)/poland(next(n))
    else:
        return float(s[n])


s = input().split()
print('%.6f' % (poland(0)))
