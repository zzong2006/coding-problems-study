from collections import deque, defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(curr, route, dist, visited):
            max_dist = dist
            max_route = route
            for k in graphs[curr]:
                if k not in visited:
                    visited.add(k)
                    route.append(k)
                    d, r = dfs(k, route, dist + 1, visited)
                    if max_dist < d:
                        max_dist = d
                        max_route = r.copy()
                    route.pop()
                    visited.remove(k)
            return max_dist, max_route

        graphs = defaultdict(list)
        for a, b in edges:
            graphs[a].append(b)
            graphs[b].append(a)
        dist, route = dfs(0, [0], 0, {0})
        dist, route = dfs(route[-1], [route[-1]], 0, {route[-1]})
        n = len(route)
        if n % 2 == 0:
            return [route[n // 2], route[n // 2 - 1]]
        else:
            return [route[n // 2]]


print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
