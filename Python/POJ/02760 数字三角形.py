N = int(input())
l = []
for i in range(N):
    l += [[0]+list(map(int, input().split()))+[0]]
for i in range(1, N):
    for j in range(1, i+2):
        l[i][j] += max(l[i-1][j], l[i-1][j-1])
print(max(l[-1]))
