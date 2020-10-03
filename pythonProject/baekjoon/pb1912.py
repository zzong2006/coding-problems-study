import sys
import heapq
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().split()))
    dp = [0] * n
    dp[0] = board[0]
    max_val = board[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1] + board[i], board[i])
        max_val = max(dp[i], max_val)
    return max_val

print(solution())