import sys


def solution():
    def build_seg_tree(curr, start, end):
        # print(curr, start, end)
        if start == end:
            seg_tree[curr] = board[start]
            return board[start]
        else:
            mid = (start + end) // 2
            seg_tree[curr * 2] = build_seg_tree(curr * 2, start, mid)
            seg_tree[curr * 2 + 1] = build_seg_tree(curr * 2 + 1, mid + 1, end)
            seg_tree[curr] = min(seg_tree[curr * 2], seg_tree[curr * 2 + 1])
            return seg_tree[curr]

    def find_min_in_seg_tree(curr, start, end, s, e):
        if end < s or start > e:
            return sys.maxsize
        else:
            if s <= start and end <= e:
                return seg_tree[curr]
            else:
                mid = (start + end) // 2
                left = find_min_in_seg_tree(curr * 2, start, mid, s, e)
                right = find_min_in_seg_tree(curr * 2 + 1, mid + 1, end, s, e)
                return min(left, right)

    get_input = sys.stdin.readline

    n, m = list(map(int, get_input().split()))
    board = []
    seg_tree = [sys.maxsize] * (n * 4)

    for i in range(n):
        board.append(int(get_input().strip()))
    build_seg_tree(1, 0, n - 1)

    for i in range(m):
        a, b = list(map(int, get_input().split()))
        ans = find_min_in_seg_tree(1, 0, n - 1, a - 1, b - 1)
        print(ans)


solution()
