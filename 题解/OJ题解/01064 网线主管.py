N, K = map(int, input().split())
l = []
ans = '0.00'
sum = 0
for i in range(0, N):
    l.append(int(float(input())*100))
    sum += l[-1]
if sum >= K:
    big = int(sum/K)+1
    small = 1
    while True:
        if big-small == 1:
            ans = format(small/100, '.2f')
            break
        count = 0
        i = int((big+small)/2)
        for a in l:
            count += int(a/i)
        if count >= K:
            small = i
        else:
            big = i
print(ans)
