n = int(input())
is_prime = [True] * (n + 1)
primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
for a in primes:
    if is_prime[n-a]:
        print('%d %d' % (a, n-a))
        break
