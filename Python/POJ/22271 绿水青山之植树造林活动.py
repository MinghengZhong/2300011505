d = {}
for _ in range(n := int(input())):
    s = input()
    d[s] = d.get(s, 0)+1
for a in sorted(d.keys()):
    print(a, '%.4f%%' % (d[a]*100/n))
