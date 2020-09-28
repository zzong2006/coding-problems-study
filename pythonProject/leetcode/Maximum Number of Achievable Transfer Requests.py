from typing import List
from itertools import combinations


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        count = 0
        for i in range(1 << len(requests)):
            ls = [0] * n
            for x in range(len(requests)):
                if (1 << x) & i != 0:
                    f, t = requests[x]
                    ls[f] -= 1
                    ls[t] += 1
            if all(v == 0 for v in ls):
                count = max(count, bin(i).count("1"))
        return count


a = Solution()
print(a.maximumRequests(5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]))

# print(a.maximumRequests(3, [[2, 2], [2, 0], [1, 1], [2, 1], [1, 1], [2, 2], [1, 0], [0, 2], [1, 2]]))
