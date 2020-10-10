import sys


def solution():
    def check(a, b):
        start = a
        end = b
        while start <= end:
            if board[start] != board[end]:
                return False
            start += 1
            end -= 1
        return True
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().strip().split()))
    m = int(get_input().strip())
    dp = [[False] * n for _ in range(n)]

    for i in reversed(range(n)):
        for j in range(i, n):
            if i == j:
                dp[i][j] = True
            else:
                if board[i] == board[j]:
                    if j - i > 1 and dp[i + 1][j - 1]:
                        dp[i][j] = True
                    elif j - i == 1:
                        dp[i][j] = True

    # for i in range(n):
    #     print(dp[i][:])
    for i in range(m):
        s, e = list(map(int, get_input().strip().split()))
        if dp[s - 1][e - 1]:
            print(1)
        else:
            print(0)


solution()
