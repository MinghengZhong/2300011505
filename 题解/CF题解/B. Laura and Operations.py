def judge(b, c):
    if (b-c) % 2 == 0:
        return '1'
    else:
        return '0'


t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    print(judge(b, c)+' '+judge(c, a)+' '+judge(a, b))
