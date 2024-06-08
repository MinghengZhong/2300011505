for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = [l[0]]
    sum = l[0]
    odd = 0
    if l[0] % 2 == 1:
        odd += 1
    for i in range(1, n):
        sum += l[i]
        if l[i] % 2 == 1:
            odd += 1
        ans.append(sum-((odd//3)+(odd % 3) % 2))
    print(' '.join(map(str, ans)))
