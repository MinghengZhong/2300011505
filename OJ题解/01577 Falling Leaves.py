class Tree:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.val = x


def build(par, x):
    if x < par.val:
        if par.left:
            build(par.left, x)
        else:
            par.left = Tree(x)
    else:
        if par.right:
            build(par.right, x)
        else:
            par.right = Tree(x)


def dfs(T):
    ans = T.val
    if T.left:
        ans += dfs(T.left)
    if T.right:
        ans += dfs(T.right)
    return ans


l = []
while True:
    s = input()
    if s in '*$':
        T = Tree(l[-1])
        for i in range(len(l)-2, -1, -1):
            for a in l[i]:
                build(T, a)
        print(dfs(T))
        if s == '$':
            break
        l = []
    else:
        l.append(s)
