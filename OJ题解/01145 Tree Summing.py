def F(S):
    n = int(S[0])
    s = []
    for i in range(1, len(S)):
        if S[i] == ')':
            if i >= 3 and S[i-3:i+1] == ['(', ')', '(', ')'] and sum(s) == n:
                return 'yes'
            elif S[i-1] != '(':
                s.pop()
        elif S[i] != '(':
            s.append(int(S[i]))
    return 'no'


S, c = [], 0
while True:
    try:
        s = input()
    except EOFError:
        break
    for a in s:
        if '0' <= a <= '9' or a == '-':
            if S and S[-1] not in '()':
                S[-1] += a
            else:
                S.append(a)
        elif a == '(':
            S.append(a)
            c += 1
        elif a == ')':
            S.append(a)
            c -= 1
            if not c:
                print(F(S))
                S = []
