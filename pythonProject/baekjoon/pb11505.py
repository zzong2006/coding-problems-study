import sys
from math import log10


def solution():
    def build_seg_tree(seg, start, end, curr):
        if start == end:
            seg[curr] = board[start]
            return board[start]
        elif start < end:
            mid = (start + end) // 2
            left = build_seg_tree(seg, start, mid, curr * 2)
            right = build_seg_tree(seg, mid + 1, end, curr * 2 + 1)
            seg[curr] = (left * right) % 1000000007
            return seg[curr]

    def get_from_b_to_c(seg, start, end, s, e, curr):
        if e < start or end < s:
            return 1
        else:
            if s <= start and end <= e:
                return seg[curr]
            else:
                mid = (start + end) // 2
                l = get_from_b_to_c(seg, start, mid, s, e, curr * 2)
                r = get_from_b_to_c(seg, mid + 1, end, s, e, curr * 2 + 1)
                return (l * r) % 1000000007

    def change_value_of_c(seg, start, end, idx, old_val, new_val, curr):
        if start == end == idx:
            seg[curr] = new_val
            return seg[curr]
        else:
            if start <= idx <= end:
                mid = (start + end) // 2
                l = change_value_of_c(seg, start, mid, idx, old_val, new_val, curr * 2)
                r = change_value_of_c(seg, mid + 1, end, idx, old_val, new_val, curr * 2 + 1)

                seg[curr] = l * r
                seg[curr] %= 1000000007
                return seg[curr]
            else:
                return seg[curr]


    get_input = sys.stdin.readline
    n, m, k = list(map(int, get_input().strip().split()))
    board = []
    seg_tree = [0] * (n * 4)
    for i in range(n):
        board.append(int(get_input().strip()))

    build_seg_tree(seg_tree, 0, n - 1, 1)

    for i in range(m + k):
        a, b, c = list(map(int, get_input().strip().split()))
        if a == 1:
            old = board[b - 1]
            board[b - 1] = c
            change_value_of_c(seg_tree, 0, n - 1, b - 1, old, c, 1)
        else:
            print(get_from_b_to_c(seg_tree, 0, n - 1, b - 1, c - 1, 1))

solution()
