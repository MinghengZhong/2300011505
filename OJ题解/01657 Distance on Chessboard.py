n = int(input())
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in range(n):
    s = input()
    x = abs(l.index(s[0])-l.index(s[3]))
    y = abs(int(s[1])-int(s[4]))

    ans1 = str(max(x, y))

    if x == 0 and y == 0:
        ans2 = '0'
    elif (x == 0 and y != 0) or (y == 0 and x != 0) or (x == y):
        ans2 = '1'
    else:
        ans2 = '2'

    if x == 0 and y == 0:
        ans3 = '0'
    elif (x == 0 and y != 0) or (y == 0 and x != 0):
        ans3 = '1'
    else:
        ans3 = '2'

    if (x+y) % 2 != 0:
        ans4 = 'Inf'
    else:
        if x == 0 and y == 0:
            ans4 = '0'
        elif x == y:
            ans4 = '1'
        else:
            ans4 = '2'

    print(ans1+' '+ans2+' '+ans3+' '+ans4)
