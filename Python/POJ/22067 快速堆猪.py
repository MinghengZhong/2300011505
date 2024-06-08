l, S = [], []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == 'min':
        if S:
            print(l[-1])
    elif s == 'pop':
        if S:
            S.pop()
            l.pop()
    else:
        n = int(s.split()[1])
        S.append(n)
        if l:
            n = min(l[-1], n)
        l.append(n)


'''
import heapq
l, S = [], []
while True:
    try:
        s = input()
    except EOFError:
        break
    if s == 'min':
        if S:
            print(l[0])
    elif s == 'pop':
        if S:
            l.remove(S.pop())
    else:
        n = int(s.split()[1])
        S.append(n)
        heapq.heappush(l, n)
'''
