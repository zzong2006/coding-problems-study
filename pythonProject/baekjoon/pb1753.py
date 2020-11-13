import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    vertex, edge = list(map(int, get_input().strip().split()))
    start = int(get_input().strip())
    graph = [[] for _ in range(vertex + 1)]
    for i in range(edge):
        u, v, w = list(map(int, get_input().strip().split()))
        graph[u].append((v, w))
    dist = [float('inf')] * (vertex + 1)

    hq = []
    dist[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        d, c = heapq.heappop(hq)
        if dist[c] < d:
            continue

        for target, distance in graph[c]:
            if dist[target] > dist[c] + distance:
                dist[target] = dist[c] + distance
                heapq.heappush(hq, (dist[target], target))

    for i in range(1, len(dist)):
        if dist[i] == float('inf'):
            print('INF')
        else:
            print(dist[i])


solution()
