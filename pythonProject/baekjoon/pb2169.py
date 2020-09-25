"""
로봇 조종하기
"""

import sys
from typing import List

sys.setrecursionlimit(10 ** 7)
get_input = sys.stdin.readline


def pretty_2d_printing(a: List[List[int]]):
    for i in range(len(a)):
        print(a[i][:])


def solution():
    n, m = list(map(int, get_input().strip().split()))
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))
    stack = []
    already = set()
    already.add((0, 0))
    stack.append([(0, 0), board[0][0], already])
    dp = [[None] * m for _ in range(n)]
    dp[0][0] = board[0][0]

    for i in range(1, m):
        dp[0][i] = dp[0][i - 1] + board[0][i]

    left = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]

    for i in range(n - 1):
        left[i][:] = dp[i][:]
        right[i][:] = dp[i][:]

        # left
        for k in reversed(range(m)):
            if k == m - 1:
                left[i + 1][k] = left[i][k] + board[i + 1][k]
            else:
                left[i + 1][k] = max(left[i][k], left[i + 1][k + 1]) + board[i + 1][k]

        # right
        for k in range(m):
            if k == 0:
                right[i + 1][k] = right[i][k] + board[i + 1][k]
            else:
                right[i + 1][k] = max(right[i][k], right[i + 1][k - 1]) + board[i + 1][k]

        # dp
        for k in range(m):
            if k == 0 or k == m - 1:
                dp[i + 1][k] = max(right[i + 1][k], left[i + 1][k])
            else:
                dp[i + 1][k] = max(dp[i][k] + board[i + 1][k], right[i + 1][k], left[i + 1][k])
    # pretty_2d_printing(dp)

    answer = dp[n - 1][m - 1]
    return answer


print(solution())
