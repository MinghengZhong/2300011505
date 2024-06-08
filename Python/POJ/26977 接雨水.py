n = int(input())
l = list(map(int, input().split()))
a = [0]*n
b = [0]*n
a[0] = l[0]
b[-1] = l[-1]
for i in range(1, n):
    a[i] = max(a[i-1], l[i])
for i in range(n-2, -1, -1):
    b[i] = max(b[i+1], l[i])
print(sum(min(a[i], b[i])-l[i] for i in range(n)))
