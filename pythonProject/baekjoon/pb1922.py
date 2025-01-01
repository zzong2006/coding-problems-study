import sys
from collections import deque
import heapq


def solution():
    def find(obj):
        w = ls[obj]
        if w != obj:
            p = find(w)
            ls[obj] = p

        return ls[obj]

    def union(inp_a, inp_b):
        x = find(inp_a)
        y = find(inp_b)
        if x != y:
            ls[x] = y
            return True
        else:
            return False

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    m = int(get_input().strip())
    graph = []
    ls = list(range(n + 1))
    for i in range(m):
        a, b, v = list(map(int, get_input().strip().split()))
        heapq.heappush(graph, (v, a, b))

    resource = 0
    while graph:
        v, a, b = heapq.heappop(graph)
        res = union(a, b)
        if res:
            resource += v
        # print(a, find(a), b, find(b))
        # print(ls)

    return resource


print(solution())
