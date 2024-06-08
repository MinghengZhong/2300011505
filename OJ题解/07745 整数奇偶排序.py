l = list(map(int, input().split()))
l1, l2 = [], []
for a in l:
    if a % 2 == 1:
        l1 += [a]
    else:
        l2 += [a]
print(' '.join(map(str, sorted(l1, reverse=True)+sorted(l2))))
