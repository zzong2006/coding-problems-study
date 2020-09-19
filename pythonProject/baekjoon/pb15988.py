dp = [0] * 1000001


def get_number(w: int):
    return dp[w]


dp[1] = 1
dp[2] = 2
dp[3] = dp[3 - 1] + dp[3 - 2] + 1 # 4
dp[4] = dp[4 - 1] + dp[4 - 2] + dp[4 - 3]  # 1 + 2 + 4 = 7
for i in range(5, 1000001):
    dp[i] += (dp[i - 3] + dp[i - 2] + dp[i - 1])
    dp[i] %= 1000000009

a = int(input())

p = [int(input()) for _ in range(a)]

ans = [get_number(x) for x in p]

print('\n'.join(list(map(str, ans))))
