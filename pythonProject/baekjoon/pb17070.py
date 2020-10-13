"""파이프 옮기기"""
import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
    # print(len(dp), len(dp[0]), len(dp[0][0]))
    # 0 가로 , 1 세로 , 2 대각선
    dp[0][1][0] = 1
    for i in range(2, n):
        if board[0][i] == 0:
            dp[0][i][0] = dp[0][i - 1][0]
    for i in range(2, n):
        if board[0][i] == 0 and board[1][i] == 0 and board[1][i - 1] == 0:
            dp[1][i][2] = dp[0][i - 1][0]
        if board[1][i] == 0:
            dp[1][i][0] = dp[1][i - 1][0] + dp[1][i - 1][2]
    for k in range(2, n):
        for i in range(2, n):
            if board[k][i] == 0:  # 세로 그리고 가로
                dp[k][i][1] = dp[k - 1][i][1] + dp[k - 1][i][2]
                dp[k][i][0] = dp[k][i - 1][0] + dp[k][i - 1][2]

            if board[k - 1][i] == 0 and board[k][i] == 0 and board[k][i - 1] == 0:
                dp[k][i][2] = dp[k - 1][i - 1][0] + dp[k - 1][i - 1][1] + dp[k - 1][i - 1][2]


    # for i in range(3):
    #     for j in range(n):
    #         for k in range(n):
    #             print(dp[j][k][i], end=" ")
    #         print()
    #     print()
    total = 0
    for i in range(3):
        total += dp[n - 1][n - 1][i]
    return total


print(solution())
