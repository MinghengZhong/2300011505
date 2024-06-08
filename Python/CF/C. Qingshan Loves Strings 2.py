def check(l):
    k = len(l)
    for i in range(k//2):
        if l[i] == l[k-i-1]:
            return False
    return True


N = int(input())
for _ in range(N):
    n = int(input())
    s = input()
    if check(s):
        print(0)
        print('')
    else:
        count = 0
        for i in s:
            if i == '1':
                count += 1
            else:
                count -= 1
        if count < -1 or count > 1:
            print('-1')
        else:
            ans = True
            count = 0
            l = []
            head = 0
            tail = n-1
            while True:
                if count == 301:
                    ans = False
                    break
                if len(s) <= 1:
                    break
                if s[head] != s[tail]:
                    head += 1
                    tail -= 1
# 后面不会了
