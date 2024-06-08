n, k = map(int, input().split())
printed = []
l = []
nums = []
for i in range(0, k):
    s = input()
    l.append(s)
    printed.append(False)
    num = 0
    for j in range(0, n):
        for kk in range(j+1, n):
            if s[kk] < s[j]:
                num += 1
    nums.append(num)
for i in range(0, k):
    minn = -1
    for j in range(0, k):
        if minn == -1 and printed[j] == False:
            minj = j
            minn = nums[j]
        elif minn > nums[j] and printed[j] == False:
            minj = j
            minn = nums[j]
    printed[minj] = True
    print(l[minj])
