import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    t: int = int(get_input().strip())
    for i in range(t):
        n: int = int(get_input().strip())
        graph = [[float('inf')] * (n + 2) for _ in range(n + 2)]
        dist = []
        for j in range(n + 2):
            dist.append(tuple(map(int, get_input().strip().split())))

        for j in range(n + 2):
            for k in range(n + 2):
                if abs(dist[j][0] - dist[k][0]) + abs(dist[j][1] - dist[k][1]) > 1000:
                    graph[j][k] = False
                else:
                    graph[j][k] = True

        for q in range(n + 2):
            for w in range(n + 2):
                for e in range(n + 2):
                    graph[w][e] = max(graph[w][e], graph[w][q] & graph[q][e])

        if graph[0][n + 1] is True:
            print('happy')
        else:
            print('sad')


solution()
