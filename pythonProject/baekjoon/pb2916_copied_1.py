import sys

input = sys.stdin.readline

n, k = map(int, input().split())
t = list(map(int, input().split()))
h = list(map(int, input().split()))

dp = [[0] * (365) for _ in range(n + 1)]
res = [0] * (361)


def func(i, j):
    if i == n:
        return
    if dp[i][j]:
        return
    dp[i][j] = 1
    res[j] = 1

    func(i, (360 + j - t[i]) % 360)
    func(i, (360 + j + t[i]) % 360)
    func(i + 1, j)


func(0, 0)

for i in range(k):
    if res[h[i]]:
        print("YES")
    else:
        print("NO")
