def count(s):
    n = 0
    for a in s:
        if a == '4' or a == '7':
            n += 1
    return n


s = input()
ss = str(count(s))
if count(ss) == len(ss):
    print('YES')
else:
    print('NO')
