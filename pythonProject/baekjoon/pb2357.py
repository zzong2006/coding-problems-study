import sys
from typing import List


def build_segment(tree, arr, left, right, curr, func):
    if left >= right:
        tree[curr] = arr[left]
    else:
        mid = int((left + right) / 2)
        tree[curr * 2] = build_segment(tree, arr, left, mid, curr * 2, func)
        tree[curr * 2 + 1] = build_segment(
            tree, arr, mid + 1, right, curr * 2 + 1, func
        )
        tree[curr] = func(tree[curr * 2], tree[curr * 2 + 1])

    return tree[curr]


def do_range_query(tree, left, right, a, b, curr, func):
    if b < left or right < a:
        if func == min:
            return sys.maxsize
        else:
            return -sys.maxsize
    else:
        if a <= left and right <= b:
            return tree[curr]
        else:
            mid = int((left + right) / 2)
            left_val = do_range_query(tree, left, mid, a, b, curr * 2, func)
            right_val = do_range_query(tree, mid + 1, right, a, b, curr * 2 + 1, func)

            return func(left_val, right_val)


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))

    nums = []
    for i in range(n):
        nums.append(int(get_input().strip()))

    # build segment tree
    min_tree = [None] * (n * 4)
    max_tree = [None] * (n * 4)

    build_segment(min_tree, nums, 0, n - 1, 1, min)
    build_segment(max_tree, nums, 0, n - 1, 1, max)

    for i in range(m):
        a, b = list(map(int, get_input().strip().split()))

        min_val = do_range_query(min_tree, 0, n - 1, a - 1, b - 1, 1, min)

        max_val = do_range_query(max_tree, 0, n - 1, a - 1, b - 1, 1, max)
        print("{} {}".format(min_val, max_val))


solution()
