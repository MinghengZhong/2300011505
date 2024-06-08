a = input()
b = ['H', 'Q', '9']
ans = False
for i in a:
    if i in b:
        ans = True
if ans:
    print('YES')
else:
    print('NO')
