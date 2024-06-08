def F(s, t, k):
    T = t
    a = s[t]
    for i in range(t, t+k+1):
        if s[i] < a:
            a = s[i]
            T = i
    return a, T+1, k-T+t


for _ in range(int(input())):
    s, k = input().split()
    s += '0'
    k = int(k)
    t = 0
    ans = ''
    while k:
        a, t, k = F(s, t, k)
        ans += a
    print((ans+s[t:])[:-1])
