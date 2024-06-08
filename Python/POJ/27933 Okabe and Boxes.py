n = int(input())
stack = []
c = 1
ans = 0
for _ in range(2*n):
    s = input()
    if s[0] == 'a':
        x = int(s.split()[1])
        stack.append(x)
    else:
        if stack[-1] != c:
            stack.sort(reverse=True)
            ans += 1
        stack.pop()
        c += 1
print(ans)
