import sys
from collections import deque


def solution():
    answer = 0
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    plan = []
    for i in range(n):
        plan.append(list(map(int, get_input().strip().split())))

    dp = [0] * (n + 1)
    for idx, [t, p] in enumerate(plan):
        answer = max(answer, dp[idx])
        if idx + t <= n:
            dp[idx + t] = max(dp[idx + t], p + answer)

    print(max(dp[-1], answer))


solution()
