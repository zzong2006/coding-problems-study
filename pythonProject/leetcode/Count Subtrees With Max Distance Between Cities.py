from collections import defaultdict
from itertools import combinations
from typing import List


class Solution:
    def countSubgraphsForEachDiameter(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        def get_maximum_distance(tong):
            def dfs(start, curr, vis, count):
                for e_in_dfs in graph[curr]:
                    if e_in_dfs in tong and e_in_dfs not in vis:
                        vis.add(e_in_dfs)
                        sample[start].append(count + 1)
                        dfs(start, e_in_dfs, vis, count + 1)

            max_val = -1
            sample = defaultdict(list)
            for elm in tong:
                visited = set()
                visited.add(elm)
                for e in graph[elm]:
                    if e in tong and e not in visited:
                        visited.add(e)
                        sample[elm].append(1)
                        dfs(elm, e, visited, 1)

            # print(tong, sample)
            for k in sample.keys():
                if len(sample[k]) != len(tong) - 1:
                    return -1
                else:
                    max_val = max(max_val, max(sample[k]))
            return max_val

        answer = [0] * (n - 1)
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        vertexes = list(range(1, n + 1))
        for i in range(2, n + 1):
            for comb in combinations(vertexes, i):
                maxi = get_maximum_distance(set(comb))
                if maxi != -1:
                    answer[maxi - 1] += 1
        return answer


helper = Solution()
print(helper.countSubgraphsForEachDiameter(4, [[1, 2], [2, 3], [2, 4]]))
