import sys

get_input = sys.stdin.readline

n = int(get_input().strip())

dp = [0] * 5001
dp[3] = 1
dp[5] = 1
for i in range(6, n + 1):
    three = 0
    five = 0
    if dp[i - 3] != 0:
        three = dp[i - 3] + 1
    if dp[i - 5] != 0:
        five = dp[i - 5] + 1
    if three and five:
        dp[i] = min(three, five)
    elif three:
        dp[i] = three
    elif five :
        dp[i] = five

# print(dp)
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])