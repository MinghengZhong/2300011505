N = int(input())
K = int(input())
T = int(input())
R = int(input())
s = [[]]*(R*K*T)
for i in range(R*K*T):
    s[i] = list(map(float, input().split()))
d = [[]]*(N*K*R)
for i in range(N*R*K):
    d[i] = list(map(float, input().split()))
J = int(input())
for i in range(J):
    l = input()
for i in range(R*K*T):
    for j in range(N):
        print('0.000000', end='')
        if j != N-1:
            print(' ', end='')
    print('')
