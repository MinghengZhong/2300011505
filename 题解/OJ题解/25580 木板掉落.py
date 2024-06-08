H, L, n = map(int, input().split())
l = sorted(list(map(int, input().split())))
print('%.2f' % (H-5*(L/l[n//2])**2))
