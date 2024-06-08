def judge(s):
    if s == []:
        return True
    for i in range(0, len(s)-1):
        if s[i+1] == s[i]:
            s.pop(i)
            s.pop(i)
            return judge(s)
    return False


n = int(input())
s = input()
ans = 0
l = []
for a in s:
    l.append(a)
for i in range(0, n-1):
    for j in range(i+1, n, 2):
        if judge(l[i:j+1]):
            ans += 1
print(ans)
