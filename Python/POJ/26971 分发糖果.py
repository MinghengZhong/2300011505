def fall(s):
    count = 0
    ss = []
    for i in range(0, len(s)-1):
        if s[i+1] > s[i]:
            if count >= 0:
                count += 1
            else:
                ss.append(count)
                count = 1
        else:
            if count <= 0:
                count -= 1
            else:
                ss.append(count)
                count = -1
    ss.append(count)
    i = 0
    ans = 0
    for i in range(len(ss)):
        if ss[i] > 0:
            if i == len(ss)-1:
                ans += int(ss[i]*(ss[i]+1)/2)
            else:
                if ss[i] > -ss[i+1]:
                    ans += int(ss[i]*(ss[i]+1)/2)
                else:
                    ans += int((ss[i]-1)*ss[i]/2)
        else:
            if i == 0:
                ans += int(-ss[i]*(-ss[i]+1)/2)
            else:
                if -ss[i] >= ss[i-1]:
                    ans += int(-ss[i]*(-ss[i]+1)/2)
                else:
                    ans += int((-ss[i]-1)*(-ss[i])/2)
    return ans


n = int(input())
l = list(map(int, input().split()))
ans = 0
start = 0
end = -1
for i in range(n-1):
    if l[i+1] == l[i]:
        if end == -1:
            end = i+1
        else:
            start = end
            end = i+1
        ans += fall(l[start: end])
if end != -1:
    ans += fall(l[end:])
else:
    ans += fall(l)
print(n+ans)
