t = int(input())
ans = [0]*t
for _ in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if k >= 3:
        continue
    l.sort()
    ll = [l[i]-l[i-1] for i in range(1, n)]
    ans[_] = min(min(ll), l[0])
    if k == 2:
        for a in l:
            left, right, count = 0, 0, ll[0]
            while True:
                ans[_] = min(ans[_], abs(count-a))
                if count < a:
                    if right == n-2:
                        break
                    right += 1
                    count += ll[right]
                elif count > a:
                    if left == right:
                        if right == n-2:
                            break
                        left += 1
                        right += 1
                        count = ll[left]
                    else:
                        count -= ll[left]
                        left += 1
                else:
                    break
for a in ans:
    print(a)
