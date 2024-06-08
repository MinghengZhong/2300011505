n = int(input())
a = list(map(int, input().split()))
count = 0
sum = 0
for i in range(0, n):
    sum += a[i]
sum = int(sum/2)+1
a.sort(reverse=True)
for i in range(0, n):
    count += a[i]
    if count >= sum:
        print(i+1)
        break
