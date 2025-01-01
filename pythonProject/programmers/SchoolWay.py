def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    puds = set()
    for x, y in puddles:
        puds.add((x - 1, y - 1))

    if (1, 0) in puds:
        dp[0][1] = 0
    else:
        dp[0][1] = 1

    if (0, 1) in puds:
        dp[1][0] = 0
    else:
        dp[1][0] = 1

    for i in range(n):
        if i == 0:
            for j in range(2, m):
                if (j, i) in puds:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1]
        elif i == 1:
            for j in range(1, m):
                if (j, i) in puds:
                    dp[i][j] = 0
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
        else:
            for j in range(m):
                if j == 0:
                    if (j, i) in puds:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i - 1][j]
                else:
                    if (j, i) in puds:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    answer = dp[n - 1][m - 1]
    return answer


print(solution(4, 6, [[1, 3]]))
