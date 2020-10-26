from collections import deque


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [[0] * 100 for _ in range(100)]
        que = deque()
        que.append((poured, 0, 0))
        while que:
            p, i, j = que.popleft()
            if p > 1:
                cups[i][j] = 1
                p -= 1
                if i + 1 < len(cups) and i + 1 <= query_row and j + 1 < len(cups[0]):
                    que.append((p / 2, i + 1, j))
                    que.append((p / 2, i + 1, j + 1))
            else:
                cups[i][j] += p

        return cups[query_row][query_glass]


a = Solution()
print(a.champagneTower(111, 1, 1))
