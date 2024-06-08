n = int(input())
l = list(map(int, input().split()))
f = ''


def dfs(x, L):
    global f
    a, b = 2*x+1, 2*x+2
    if a >= n and b >= n:
        print(*L)
        return
    for y in (b, a):
        if y < n:
            if l[y] > L[-1]:
                ff = 'Min Heap'
            else:
                ff = 'Max Heap'
            if not f:
                f = ff
            elif ff != f:
                f = 'Not Heap'
            dfs(y, L+[l[y]])
    return


dfs(0, [l[0]])
print(f)
