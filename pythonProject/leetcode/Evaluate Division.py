from collections import defaultdict
from typing import List


def recur(graph, adj, to, goal, visit):
    if to not in adj:
        return -1
    elif (to, goal) in graph:
        return graph[(to, goal)]
    else:
        visit.add(to)
        for z in adj[to]:
            if (to, z) in graph and z not in visit:
                new_visit = visit.copy()
                new_visit.add(z)
                val = recur(graph, adj, z, goal, new_visit)
                if val != -1:
                    return graph[(to, z)] * val
        else:
            return -1


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = dict()
        adj = dict()
        for [aa, bb], val in zip(equations, values):
            if aa != bb:
                graph[(aa, bb)] = val
                graph[(bb, aa)] = 1 / val
                if aa not in adj:
                    adj[aa] = list()
                if bb not in adj:
                    adj[bb] = list()
                adj[aa].append(bb)
                adj[bb].append(aa)
        print(adj)
        for [qq, ww] in queries:
            val = recur(graph, adj, qq, ww, set())
            result.append(val)
        return result


a = Solution()

print(a.calcEquation([["a", "b"], ["b", "c"]],
                     [2.0, 3.0],
                     [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))

b = defaultdict(dict)
b["test"]["test"] = 2
print(b)

