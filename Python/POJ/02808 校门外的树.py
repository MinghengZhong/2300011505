ans, n = map(int, input().split())
ans += 1
trees = []
for i in range(0, ans+1):
    trees.append(True)
for i in range(0, n):
    start, stop = map(int, input().split())
    for j in range(start, stop+1):
        if trees[j]:
            trees[j] = False
            ans -= 1
print(ans)
