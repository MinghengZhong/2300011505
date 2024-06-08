s = []
for _ in range(int(input())):
    s.append(input())
print('\n'.join(sorted(s, key=lambda x: list(map(int, x.split('.'))))))
