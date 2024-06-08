n = int(input())
x = []
h = []
for i in range(n):
    xi, hi = map(int, input().split())
    x.append(xi)
    h.append(hi)
ans = 1
right = False
for i in range(1, n):
    if i == n-1:
        ans += 1
    else:
        if right:
            if x[i]-h[i] > x[i-1]+h[i-1]:
                ans += 1
                right = False
            elif x[i]+h[i] < x[i+1]:
                ans += 1
                right = True
            else:
                right = False
        else:
            if x[i]-h[i] > x[i-1]:
                ans += 1
                right = False
            elif x[i]+h[i] < x[i+1]:
                ans += 1
                right = True
            else:
                right = False
print(ans)
