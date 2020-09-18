def solution(triangle):
    dp = [[0] * len(n) for n in triangle]
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0 :
                dp[i][j] = dp[i - 1][j] + triangle[i][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
    answer = max(dp[len(triangle) - 1])
    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))