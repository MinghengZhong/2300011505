class Tree:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        mid = self.val
        left = right = ''
        if self.left:
            left = str(self.left)
            if mid == '*' and self.left.val == '+':
                left = '('+left+')'
        if self.right:
            right = str(self.right)
            if mid == '*' and self.right.val == '+':
                right = '('+right+')'
        return left+mid+right


def build(l, i, n):
    stack = []
    temp = ''
    while i < len(l) and n:
        if l[i] == ')':
            i += 1
            break
        elif l[i] == '(':
            s, i = build(l, i+1, -1)
            stack.append(s)
            n -= 1
        elif l[i] == '+':
            if temp:
                stack.append(Tree(temp, stack.pop(), stack.pop()))
            temp = '+'
            i += 1
        elif l[i] == '*':
            if temp:
                s, i = build(l, i+1, 1)
                stack.append(Tree('*', s, stack.pop()))
            else:
                temp = '*'
                i += 1
        else:
            stack.append(Tree(l[i]))
            n -= 1
            i += 1
    if temp:
        return Tree(temp, stack.pop(), stack.pop()), i
    else:
        return stack.pop(), i


while True:
    try:
        s = input()
    except EOFError:
        break
    num = ''
    l = []
    for a in s:
        if '0' <= a <= '9':
            num += a
        else:
            if num:
                l.append(num)
                num = ''
            l.append(a)
    if num:
        l.append(num)
    s, i = build(l, 0, -1)
    print(str(s))
