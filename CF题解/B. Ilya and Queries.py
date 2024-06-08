s = input()+'a'
L = [0]*(len(s))
for i in range(len(s)-1):
    L[i+1] += L[i]
    if s[i] == s[i+1]:
        L[i+1] += 1
n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    print(L[r-1]-L[l-1])
