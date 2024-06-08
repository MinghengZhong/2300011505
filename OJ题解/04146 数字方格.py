n = int(input())
ans = 0
for a1 in range(n, -1, -1):
    for a2 in range(n, -1, -1):
        for a3 in range(n, -1, -1):
            if a1+a2+a3 > ans:
                if (a1+a2) % 2 == 0 and (a2+a3) % 3 == 0 and (a1+a2+a3) % 5 == 0:
                    ans = a1+a2+a3
print(ans)
