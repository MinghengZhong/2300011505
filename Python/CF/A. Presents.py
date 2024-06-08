n = int(input())
s = list(map(int, input().split()))
for i in range(0, len(s)):
    print(s.index(i+1)+1, end='')
    if i != len(s):
        print(' ', end='')
