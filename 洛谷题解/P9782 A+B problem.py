l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
s, t = input().split()
ans = l.index(s)+l.index(t)
if ans == 0:
    print('A')
elif 0 < ans <= 25:
    print(l[ans])
else:
    print(l[ans//26]+l[ans % 26])
