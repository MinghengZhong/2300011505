t = int(input())
ans = [1]*t
for _ in range(t):
    n = int(input())
    while n > 0:
        d = n % 10
        n //= 10
        count = 0
        for i in range(d+1):
            for j in range(d+1):
                if d-i-j >= 0:
                    count += 1
        ans[_] *= count
for a in ans:
    print(a)
