for i in range(0, 5):
    l = input().split()
    for j in range(0, 5):
        if l[j] == '1':
            ans = abs((i-2))+abs((j-2))
print(ans)
