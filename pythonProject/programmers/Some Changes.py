def solution(n, money):
    dp = [0] * (n + 1)

    dp[0] = 1
    money.sort()
    for m in money:
        for i in range(0, n + 1):
            if m <= i:
                dp[i] += dp[i - m]

    answer = dp[n]
    return answer


print(solution(5, [1, 2, 5]))
