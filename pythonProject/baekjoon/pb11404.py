import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    m = int(get_input().strip())

    graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        u, v, w = list(map(int, get_input().strip().split()))
        graph[u][v] = min(graph[u][v], w)
    for i in range(1, n + 1):
        graph[i][i] = 0

    # print(graph)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == float("inf"):
                print(0, end=" ")
            else:
                print(graph[i][j], end=" ")
        print()


solution()
