m, n = map(int, input().split())
is_prime = [True] * (10000 + 1)
primes = []
for i in range(2, 10000):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, 10000, i):
            is_prime[j] = False
for _ in range(m):
    l = tuple(map(int, input().split()))
    count = 0
    for a in l:
        if int(a**.5) == a**.5:
            if is_prime[int(a**.5)]:
                count += a
    print('%.2f' % (count/len(l)))
