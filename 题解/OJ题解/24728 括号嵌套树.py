from collections import defaultdict
dic = defaultdict(lambda: [])


def build(root, s):
    global dic
    count = 0
    new_root = new_leaf = ''
    for i in range(len(s)):
        if s[i] == ')':
            count -= 1
        if s[i] not in '(),' and not count:
            if new_leaf:
                build(new_root, new_leaf)
                new_leaf = ''
            new_root = s[i]
            dic[root].append(s[i])
        if count:
            new_leaf += s[i]
        if s[i] == '(':
            count += 1
    if new_leaf:
        build(new_root, new_leaf)


def pre(root):
    global dic
    temp = ''
    for leaf in dic[root]:
        temp += pre(leaf)
    return root+temp


def suf(root):
    global dic
    temp = ''
    for leaf in dic[root]:
        temp += suf(leaf)
    return temp+root


s = input()
build(s[0], s[2:-1] if len(s) > 1 else '')
print(pre(s[0]))
print(suf(s[0]))
