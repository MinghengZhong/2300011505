from collections import deque
n, m = map(int, input().split())
l = list(map(int, input().split()))
q = deque([i for i in range(n)])
while len(q)-1:
    Q = q.popleft()
    l[Q] -= m
    if l[Q] > 0:
        q.append(Q)
print(q[0]+1)
