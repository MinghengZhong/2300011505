def judge(n):
    s = str(n)
    for a in s:
        if a != '4' and a != '7':
            return False
    return True


n = int(input())
ans = False
for i in range(1, int(n/2)+1):
    if n % i == 0 and judge(int(n/i)) == True:
        ans = True
        break
if ans:
    print('YES')
else:
    print('NO')
