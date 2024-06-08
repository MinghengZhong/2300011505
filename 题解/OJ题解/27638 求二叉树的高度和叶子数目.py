left, right = [], []
height, leaf = 0, 0
not_root = set()


def dfs(x, h):
    global left, right, height
    if left[x]+1:
        dfs(left[x], h+1)
    if right[x]+1:
        dfs(right[x], h+1)
    height = max(height, h)


n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    left.append(l)
    right.append(r)
    not_root.add(l)
    not_root.add(r)
    if l == r == -1:
        leaf += 1
for root in range(n):
    if root not in not_root:
        dfs(root, 0)
print('%d %d' % (height, leaf))
