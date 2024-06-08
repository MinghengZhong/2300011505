'''
n = 10 ** 8
num_list = [True] * (n + 3)
prime_list = []
for i in range(2, n + 1):
    if num_list[i]:
        prime_list.append(i)
    for j in range(0, len(prime_list)):
        if prime_list[j] * i > n:
            break
        num_list[prime_list[j] * i] = False
        if i % prime_list[j] == 0:
            break
'''
n = 10**8
a = [2]
c = [True]*n
for i in range(1, n+1, 2):
    c[i] = False
c[0] = False
for i in range(3, n+1, 2):
    if c[i-1]:
        a.append(i)
        j = i
        while j*i <= n:
            c[j*i-1] = False
            j += 2
