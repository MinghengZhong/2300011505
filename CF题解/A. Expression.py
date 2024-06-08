def bigger(a, b):
    if a >= b:
        return a
    else:
        return b


a = int(input())
b = int(input())
c = int(input())
ans = bigger(a+b+c, a+b*c)
ans = bigger(ans, a*b+c)
ans = bigger(ans, a*b*c)
ans = bigger(ans, (a+b)*c)
ans = bigger(ans, a*(b+c))
print(ans)
