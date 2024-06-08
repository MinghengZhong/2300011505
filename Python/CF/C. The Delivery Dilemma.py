t = int(input())
output = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(b) <= min(a):
        output.append(sum(b))
    else:
        a, b = zip(*sorted(zip(a, b), reverse=True))
        ans = a[0]
        count = 0
        for i in range(n-1):
            count += b[i]
            new_ans = max(count, a[i+1])
            if new_ans < ans:
                ans = new_ans
            elif new_ans > ans:
                break
        output.append(ans)
for i in range(t):
    print(output[i])
