n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))+[m]
on = []
off = []
for i in range(n+1):
    l[i] = l[i+1]-l[i]
    if i % 2 == 0:
        on.append(l[i])
        off.append(0)
    else:
        on.append(0)
        off.append(l[i])
for i in range(1, n+1):
    on[i] += on[i-1]
    off[i] += off[i-1]
maxans = on[-1]
for i in range(n+1):
    if l[i] > 1:
        maxans = max(maxans, on[i//2*2]-1+off[-1]-off[i//2*2])
print(maxans)
