def check(l):
    for i in range(len(l)-1):
        if l[i+1] == l[i]:
            return False
    return True


N = int(input())
for _ in range(N):
    n, m = map(int, input().split())
    s = input()
    t = input()
    if check(s):
        print('Yes')
    else:
        if not check(t):
            print('No')
        else:
            ans = True
            for i in range(n-1):
                if s[i+1] == s[i]:
                    if s[i] == t[0] or s[i+1] == t[-1]:
                        ans = False
                        break
            if ans:
                print('Yes')
            else:
                print('No')
