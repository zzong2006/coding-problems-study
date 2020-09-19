# segmentation tree problem
from sys import stdin

seg_tree = []
arr = []


def build_seg_tree(start, end, curr):

    if start == end:
        seg_tree[curr] = arr[start]
    else:
        mid = int((start + end) / 2)
        seg_tree[curr] = build_seg_tree(start, mid, curr * 2) + build_seg_tree(mid + 1, end, curr * 2 + 1)
    return seg_tree[curr]


def get_range_sum(start, end, left, right, curr):
    if left <= start and end <= right:
        return seg_tree[curr]
    elif end < left or right < start:
        return 0
    else:
        mid = int((start + end) / 2)
        return get_range_sum(start, mid, left, right, curr * 2) + get_range_sum(mid + 1, end, left, right, curr * 2 + 1)


def modify_seg_tree(start, end, idx, val, curr):
    if start <= idx <= end:
        seg_tree[curr] += val
        if start == end :
            return
        mid = int((start + end) / 2)
        modify_seg_tree(start, mid, idx, val, curr * 2)
        modify_seg_tree(mid + 1, end, idx, val, curr * 2 + 1)
    else:
        return

N, M, K = list(map(int, stdin.readline().split()))
seg_tree = [0] * (N * 4)

for i in range(N):
    arr.append(int(stdin.readline()))

build_seg_tree(0, len(arr) - 1, 1)
# print(seg_tree)

for i in range(M + K):
    T, a, b = list(map(int, stdin.readline().split()))
    if T == 1:  # modify
        diff_val = b - arr[a - 1]
        modify_seg_tree(0, len(arr) - 1, a - 1, diff_val, 1)
        arr[a - 1] = b
    else:  # range sum
        print(get_range_sum(0, len(arr) - 1, a - 1, b - 1, 1))
