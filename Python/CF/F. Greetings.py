def merge_sort(l):
    if len(l) <= 1:
        return l, 0
    mid = len(l) // 2
    left, left_count = merge_sort(l[:mid])
    right, right_count = merge_sort(l[mid:])
    merged, split_count = merge(left, right)
    return merged, left_count + right_count + split_count


def merge(left, right):
    result = []
    split_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            split_count += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, split_count


for _ in range(int(input())):
    n = int(input())
    a, b = [0]*n, [0]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a, b = zip(*sorted(zip(a, b), key=lambda x: x[0]))
    b, ans = merge_sort(list(b))
    print(ans)
