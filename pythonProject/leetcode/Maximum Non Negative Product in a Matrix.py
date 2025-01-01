from typing import List


class Solution:
    test = -1

    def maxProductPath(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        np = [[0] * M for _ in range(N)]
        mp = [[0] * M for _ in range(N)]
        np[0][0] = mp[0][0] = grid[0][0]
        for i in range(1, M):
            np[0][i] = np[0][i - 1] * grid[0][i]
            mp[0][i] = mp[0][i - 1] * grid[0][i]

        for j in range(1, N):
            np[j][0] = np[j - 1][0] * grid[j][0]
            mp[j][0] = mp[j - 1][0] * grid[j][0]

        for i in range(1, N):
            for j in range(1, M):
                if grid[i][j] < 0:
                    np[i][j] = max(mp[i - 1][j], mp[i][j - 1]) * grid[i][j]
                    mp[i][j] = min(np[i - 1][j], np[i][j - 1]) * grid[i][j]
                else:
                    np[i][j] = min(np[i - 1][j], np[i][j - 1]) * grid[i][j]
                    mp[i][j] = max(mp[i - 1][j], mp[i][j - 1]) * grid[i][j]

        if mp[N - 1][M - 1] < 0:
            return -1
        else:
            return mp[N - 1][M - 1] % (10**9 + 7)


a = Solution()
print(a.maxProductPath([[1, -2, 3], [1, -2, 4], [-2, 1, 1]]))
