def L(n, m):
    return ['('*i+s for i in range(n, 0, -1) for s in R(n-i, m+i)]


def R(n, m):
    if n:
        return [')'*i+s for i in range(1, m+1) for s in L(n, m-i)]
    return [')'*m]


print('\n'.join(L(int(input()), 0)))
