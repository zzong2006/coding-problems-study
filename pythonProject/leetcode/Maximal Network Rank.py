from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        new_roads = defaultdict(list)

        for a, b in roads:
            new_roads[a].append(b)
            new_roads[b].append(a)

        ranks = []
        for a, b in combinations(new_roads.keys(), 2):
            # print((a, b))
            count = len(new_roads[a]) + len(new_roads[b])
            if b in new_roads[a]:
                count -= 1
            ranks.append(count)
        # print(ranks)
        if ranks:
            return max(ranks)
        else:
            return 0
        # return max(ranks)


a = Solution()
print(a.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]))
print(a.maximalNetworkRank(8, [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]))
