def get_father(u, par, dis):
    if par[u] != u:
        temp = par[u]
        par[u] = get_father(par[u], par, dis)
        dis[u] ^= dis[temp]
    return par[u]


for _ in range(int(input())):
    n, m = map(int, input().split())
    par = [i for i in range(n + 1)]
    dis = [0] * (n + 1)
    c = 1
    for i in range(m):
        s = input().split()
        a = ta = int(s[1])
        b = tb = int(s[2])
        a = get_father(a, par, dis)
        b = get_father(b, par, dis)
        if s[0] == 'A':
            if a != b:
                print('Not sure yet.')
            elif dis[ta] != dis[tb]:
                print('In different gangs.')
            else:
                print('In the same gang.')
        else:
            if a != b:
                par[b] = a
                dis[b] = 1 ^ dis[ta] ^ dis[tb]
