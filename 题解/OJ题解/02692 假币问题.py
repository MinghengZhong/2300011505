n = int(input())
for _ in range(n):
    left = []
    right = []
    dic = {'A': False, 'B': False, 'C': False, 'D': False,
           'E': False, 'F': False, 'G': False, 'H': False,
           'I': False, 'J': False, 'K': False, 'L': False}
    for i in range(3):
        s = input().split(' ')
        if s[2] == 'even':
            for a in s[0]:
                dic[a] = True
            for a in s[1]:
                dic[a] = True
        else:
            if s[2] == 'up':
                left.append(s[0])
                right.append(s[1])
            else:
                left.append(s[1])
                right.append(s[0])
    for a in dic.keys():
        if not dic[a]:
            b = True
            for i in left:
                if a not in i:
                    b = False
                    break
            if b:
                print(a+' is the counterfeit coin and it is heavy.')
                break
            b = True
            for i in right:
                if a not in i:
                    b = False
                    break
            if b:
                print(a+' is the counterfeit coin and it is light.')
                break
