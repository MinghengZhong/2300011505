n = int(input())
ans1 = 0
ans2 = 0
while n != 0:
    ans1 += 1
    if n % 3 == 0:
        n = (n//3)*2
    elif n % 3 == 1:
        n = (n//3)*2
        if ans2 == 0:
            ans2 = ans1
    elif n % 3 == 2:
        n = (n//3)*2+1
print('%d %d' % (ans1, ans2))
