def find(a, b):
    global ans
    if b != '':
        ans += b[-1]
        n = a.index(b[-1])
        find(a[:n], b[:n])
        find(a[n+1:], b[n:-1])


ans = ''
a = input()
aaa = ''
for aa in a:
    if 'A' <= a <= 'Z':
        aaa += aa
b = input()
bbb = ''
for bb in b:
    if 'A' <= b <= 'Z':
        bbb += bb
find(aaa, bbb)
print(ans)
