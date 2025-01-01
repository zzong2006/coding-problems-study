import sys


def solution():
    def sum_tuple(a, b):
        return a[0] + b[0], a[1] + b[1]

    get_input = sys.stdin.readline
    dp = [(0, 0)] * 41
    dp[0] = (1, 0)
    dp[1] = (0, 1)
    for k in range(41 - 2):
        dp[k + 2] = sum_tuple(dp[k], dp[k + 1])
    n = int(get_input().strip())

    for i in range(n):
        k = int(get_input().strip())
        print("{} {}".format(dp[k][0], dp[k][1]))


solution()
