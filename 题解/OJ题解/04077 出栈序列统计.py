def L(n, m):
    return sum(R(n-i, m+i) for i in range(n, 0, -1))


def R(n, m):
    return sum(L(n, m-i) for i in range(1, m+1)) if n else 1


print(L(int(input()), 0))
