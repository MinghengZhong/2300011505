def read(s, l, r):
    word, count, stack = '', 0, []
    for a in s:
        if a == r:
            count -= 1
        if count:
            stack.append(a)
        if a == l:
            count += 1
        if stack and not count:
            word += read(stack[::-1], r, l)
            stack = []
        if count == 0 and a not in '()':
            word += a
    if stack:
        word += read(stack[::-1], r, l)
    return word


s = input()
print(read(s, '(', ')'))
