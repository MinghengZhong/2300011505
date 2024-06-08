def t(n):
    if n == 1:
        return [' /\\', '/__\\']
    T = t(n-1)
    N = 2**(n-1)
    return [' '*N+T[i] for i in range(N)]+[T[i]+' '*(N-1-i)+T[i] for i in range(N)]


while True:
    n = int(input())
    if not n:
        break
    print('\n'.join(t(n)), end='\n\n')
