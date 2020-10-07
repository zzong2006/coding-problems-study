import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = list(map(int, get_input().strip().split()))[0]
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))

    dp = [0] * (n + 1)

    for i in range(n):
        t, p = board[i]
        if n >= i + t:
            dp[i + t] = max(dp[i] + p, dp[i + t])
        if n >= i + 1:
            dp[i + 1] = max(dp[i], dp[i + 1])

    answer = max(dp)

    return answer


print(solution())
