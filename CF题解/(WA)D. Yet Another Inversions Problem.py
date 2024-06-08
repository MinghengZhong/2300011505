t = int(input())
N = 998244353
ans = [0]*t


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = merge_sort(arr[:mid])
    right, right_inv = merge_sort(arr[mid:])
    merged, split_inv = merge(left, right)
    total_inv = left_inv + right_inv + split_inv
    return merged, total_inv


def merge(left, right):
    merged = []
    split_inv = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inv += len(left) - i
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, split_inv


def count_inversions(arr):
    _, inversions = merge_sort(arr)
    return inversions


for _ in range(t):
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    ans[_] += (count_inversions(q)*n) % N

for a in ans:
    print(a)
