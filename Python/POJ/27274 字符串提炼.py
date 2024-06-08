from math import log2
s = input()
m = int(log2(len(s)))
ans = ''
for i in range(m+1):
    ans += s[(1 << i)-1]
for i in range(len(ans)//2):
    print(ans[i]+ans[-i-1], end='')
if len(ans) % 2 == 1:
    print(ans[len(ans)//2])
else:
    print('')
