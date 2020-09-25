import sys


def merge_sort(arr_ds, start, end):
    if start >= end:
        return
    else:
        mid = int((start + end) / 2)
        merge_sort(arr_ds, start, mid)
        merge_sort(arr_ds, mid + 1, end)
        _merge_sort(arr_ds, start, mid, end)


def _merge_sort(arr_ms, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    curr = 0
    left = [0] * n1
    right = [0] * n2

    for k in range(n1):
        left[k] = arr_ms[start + k]

    for k in range(n2):
        right[k] = arr_ms[mid + 1 + k]

    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr_ms[k] = left[i]
            i += 1
        else:
            arr_ms[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr_ms[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr_ms[k] = right[j]
        j += 1
        k += 1


get_input = sys.stdin.readline

t = int(get_input().strip())

for i in range(t):
    n = int(get_input().strip())
    arr = list(map(int, get_input().split()))
    swap = 0

    merge_sort(arr, 0, len(arr) - 1)
    print(arr)
    th = (n * (n - 1)) / 2 - 1
    if swap > th:
        print("NO")
    else:
        print("YES")
