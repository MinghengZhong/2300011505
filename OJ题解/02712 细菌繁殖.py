n = int(input())
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(n):
    m1, d1, ans, m2, d2 = map(int, input().split())
    count = d2-d1
    for j in range(m1-1, m2-1):
        count += days[j]
    print(ans*(2**count))
