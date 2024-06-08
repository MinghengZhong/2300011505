n = 0
m = 0
l = []
memory = []
longest = []
x = 0
y = 0
back = False


def search(top):
    global n, m, l, memory, longest, x, y, back
    if len(memory) == 1 and back:
        return
    back = True
    if x+1 < m:
        if l[y][x+1] > l[y][x]:
            if [x+1, y] in longest:
                if len(memory) > longest.index([x+1, y]):
                    longest = memory+longest[longest.index([x+1, y]):]
            else:
                top = False
                x += 1
                memory.append([x, y])
                search(True)
                memory.pop()
                x -= 1
    if y+1 < n:
        if l[y+1][x] > l[y][x]:
            if [x, y+1] in longest:
                if len(memory) > longest.index([x, y+1]):
                    longest = memory+longest[longest.index([x, y+1]):]
            else:
                top = False
                y += 1
                memory.append([x, y])
                search(True)
                memory.pop()
                y -= 1
    if x-1 >= 0:
        if l[y][x-1] > l[y][x]:
            if [x-1, y] in longest:
                if len(memory) > longest.index([x-1, y]):
                    longest = memory+longest[longest.index([x-1, y]):]
            else:
                top = False
                x -= 1
                memory.append([x, y])
                search(True)
                memory.pop()
                x += 1
    if y-1 >= 0:
        if l[y-1][x] > l[y][x]:
            if [x, y-1] in longest:
                if len(memory) > longest.index([x, y-1]):
                    longest = memory+longest[longest.index([x, y-1]):]
            else:
                top = False
                y -= 1
                memory.append([x, y])
                search(True)
                memory.pop()
                y += 1
    if top:
        if len(memory) > len(longest):
            longest = []
            for ll in memory:
                longest.append(ll)
    return


n, m = map(int, input().split())
for _ in range(n):
    l.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if [j, i] not in longest:
            x = j
            y = i
            memory = [[j, i]]
            back = False
            search(True)
print(len(longest))
