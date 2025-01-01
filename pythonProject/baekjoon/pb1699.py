import math
import sys
from collections import Counter, defaultdict


def solution():
    get_input = sys.stdin.readline
    n = list(map(int, get_input().strip().split()))[0]
    sqrt_n = int(math.sqrt(n))
    squares = [0] * (sqrt_n + 1)
    for i in range(sqrt_n + 1):
        squares[i] = i**2
    dp = [sys.maxsize] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        min_val = sys.maxsize
        for j in range(1, len(squares)):
            if i >= squares[j]:
                min_val = min(min_val, dp[i - squares[j]] + 1)
            else:
                break
        dp[i] = min_val
    # print(dp)
    return dp[n]


print(solution())
