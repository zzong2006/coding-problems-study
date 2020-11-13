import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    m = int(get_input().strip())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b, t = list(map(int, get_input().strip().split()))
        graph[a].append((b, t))
    start, end = list(map(int, get_input().strip().split()))
    dist = [float('inf')] * (n + 1)
    que = []
    dist[start] = 0
    heapq.heappush(que, (0, start))
    while que:
        d, c = heapq.heappop(que)

        if dist[c] < d:
            continue
        else:
            for a, t in graph[c]:
                if dist[a] > dist[c] + t:
                    dist[a] = dist[c] + t
                    heapq.heappush(que, (dist[a], a))
    # print(dist)
    return dist[end]


print(solution())
