def compare(s1, s2):
    if int(s1+s2) > int(s2+s1):
        return 1
    elif int(s1+s2) < int(s2+s1):
        return -1
    else:
        return 0


def quicksort(l):
    if len(l) <= 1:
        return l
    ll = l[int(len(l)/2)]
    left = [x for x in l if compare(x, ll) == -1]
    middle = [x for x in l if compare(x, ll) == 0]
    right = [x for x in l if compare(x, ll) == 1]
    return quicksort(left) + middle + quicksort(right)


n = int(input())
l = quicksort(input().split())
for i in range(n-1, -1, -1):
    print(l[i], end='')
print(' ', end='')
for i in range(n):
    print(l[i], end='')
print('')
