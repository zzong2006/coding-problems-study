from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        dp = [[0] * n for _ in range(len(target))]
        memo = dict()
        for i in range(m):
            for j in range(i, n):
                if (target[i], j) not in memo:
                    for k in range(len(words)):
                        if words[k][j] == target[i]:
                            dp[i][j] += 1
                    memo[(target[i], j)] = dp[i][j]
                else:
                    dp[i][j] = memo[(target[i], j)]
                if i > 0:
                    dp[i][j] *= dp[i - 1][j - 1]
                dp[i][j] += dp[i][j - 1]
                dp[i][j] %= 10**9 + 7

        return dp[m - 1][n - 1] % (10**9 + 7)


a = Solution()
print(a.numWays(["acca", "bbbb", "caca"], "aba"))
print(a.numWays(["abba", "baab"], "bab"))
print(a.numWays(["abcd"], "abcd"))
print(a.numWays(["abab", "baba", "abba", "baab"], "abba"))
