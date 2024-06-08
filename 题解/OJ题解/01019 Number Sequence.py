n = int(input())
for iii in range(0, n):
    ii = int(input())
    count = 0
    num = 0
    j = 0
    while count < ii:
        j += 1
        num = j*len(str(j))
        for i in range(0, len(str(j))):
            num -= 10**i-1
        count += num
    count -= num
    for i in range(1, j+1):
        count += len(str(i))
        if count >= ii:
            break
    count -= len(str(i))
    ii -= count
    print(str(i)[ii-1])
