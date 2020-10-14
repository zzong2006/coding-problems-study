import heapq
import sys
from collections import Counter, defaultdict, deque


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().strip().split()))
    dp = [0] * n

    for i in reversed(range(n)):
        max_len = 0
        for j in reversed(range(i, n)):
            if board[i] > board[j] and max_len < dp[j]:
                max_len = dp[j]
        dp[i] = max_len + 1
    # print(dp)
    return max(dp)


print(solution())
