n = input()
k = int(input())
ans = []
while True:
    if k == 0:
        ans += n
        break
    elif k == len(n):
        break
    min = 'a'
    for i in range(0, k+1):
        if n[i] < min:
            min = n[i]
            mini = i
    k -= mini
    ans += n[mini]
    n = n[mini+1:]
i = 0
while ans[i] == '0' and i != len(ans)-1:
    i += 1
for j in range(i, len(ans)):
    print(ans[j], end='')
