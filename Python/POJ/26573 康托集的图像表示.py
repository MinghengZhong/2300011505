def c(n):
    return c(n-1)+'-'*(3**(n-1))+c(n-1) if n else '*'


print(c(int(input())))
