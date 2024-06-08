N = int(input())
for _ in range(N):
    n, m, b = map(int, input().split())
    damage = {}
    for i in range(n):
        t, x = map(int, input().split())
        if t not in damage.keys():
            damage[t] = [x]
        else:
            damage[t].append(x)
    damage = dict(sorted(damage.items()))
    for i in damage.keys():
        if len(damage[i]) <= m:
            b -= sum(damage[i])
        else:
            dmg = sorted(damage[i], reverse=True)
            b -= sum(dmg[0:m])
        if b <= 0:
            print(i)
            break
    if b > 0:
        print('alive')
