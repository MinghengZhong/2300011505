n = int(input())
i = 1
while i <= n:
    i += 1
    s = input()
    if len(s) <= 10:
        print(s)
    else:
        print(s[0]+str(len(s)-2)+s[-1])
