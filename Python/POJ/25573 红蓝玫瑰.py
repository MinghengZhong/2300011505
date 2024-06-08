s = list(input())
j, ans = 0, 0
c = ['R', 'B']
for i in range(len(s)-1, -1, -1):
    if s[i] != c[j]:
        ans += 1
        if i > 0 and s[i-1] != c[j]:
            j = (j+1) % 2
print(ans)
