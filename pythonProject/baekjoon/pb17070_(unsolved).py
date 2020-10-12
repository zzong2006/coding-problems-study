"""파이프 옮기기"""
import sys
from collections import deque


def solution():
    def diag_check(a, b):
        for add_y, add_x in [(0, 1), (1, 0), (1, 1)]:
            new_a = add_y + a
            new_b = add_x + b
            if not (0 <= new_a < n and 0 <= new_b < n and board[new_a][new_b] == 0):
                return False
        return True

    def right_check(a, b):
        for add_y, add_x in [(0, 1)]:
            new_a = add_y + a
            new_b = add_x + b
            if not (0 <= new_a < n and 0 <= new_b < n and board[new_a][new_b] == 0):
                return False
        return True

    def down_check(a, b):
        for add_y, add_x in [(1, 0)]:
            new_a = add_y + a
            new_b = add_x + b
            if not (0 <= new_a < n and 0 <= new_b < n and board[new_a][new_b] == 0):
                return False
        return True

    def visited(a, b, way):
        if a == n - 1 and b == n - 1:
            return False
        else:
            if (a, b, way) in already:
                return True
            else:
                return False

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))
    que = deque()
    que.append((0, 1, 'h'))
    already = set()
    count = 0
    while que:
        y, x, d = que.popleft()
        if y == n - 1 and x == n - 1:
            count += 1
        else:
            if d == 'h':
                if right_check(y, x):
                    que.append((y, x + 1, 'h'))
                if diag_check(y, x):
                    que.append((y + 1, x + 1, 'd'))
            elif d == 'd':
                if right_check(y, x):
                    que.append((y, x + 1, 'h'))
                if diag_check(y, x):
                    que.append((y + 1, x + 1, 'd'))
                if down_check(y, x):
                    que.append((y + 1, x, 'v'))
            elif d == 'v':
                if down_check(y, x):
                    que.append((y + 1, x, 'v'))
                if diag_check(y, x):
                    que.append((y + 1, x + 1, 'd'))
    return count


print(solution())
