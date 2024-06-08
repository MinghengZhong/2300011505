n, m = map(int, input().split())
print(n*(n-1)//2-len({input() for _ in range(m)}))
