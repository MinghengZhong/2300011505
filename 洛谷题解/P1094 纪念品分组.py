w = int(input())
n = int(input())
small = []
big = []
ans = 0
for _ in range(n):
    a = int(input())
    if a <= w/2:
        small.append(a)
    else:
        big.append(a)
small.sort(reverse=True)
big.sort()
while True:
    if len(small) == 0 or len(big) == 0:
        break
    if small[-1]+big[-1] <= w:
        small.pop()
    big.pop()
    ans += 1
print(ans+len(small)//2+len(small) % 2+len(big))
