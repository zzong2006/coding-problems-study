# https://www.acmicpc.net/problem/1238 (파티)

import heapq
import sys


def solution():
    def get_distance_from_a(a):
        distance = [float("inf")] * (n + 1)
        que = []
        distance[a] = 0
        heapq.heappush(que, (distance[a], a))

        while que:
            _, c = heapq.heappop(que)

            for key in graph[c].keys():
                if distance[key] > distance[c] + graph[c][key]:
                    distance[key] = distance[c] + graph[c][key]
                    heapq.heappush(que, (distance[c], key))

        return distance

    get_input = sys.stdin.readline
    n, m, x = list(map(int, get_input().split()))
    graph = [dict() for _ in range(n + 1)]
    for i in range(m):
        a, b, t = list(map(int, get_input().split()))
        graph[a][b] = t

    # start from x
    dist = [0]
    h = get_distance_from_a(x)
    for i in range(1, n + 1):
        if i == x:
            dist.append(0)
        else:
            w = get_distance_from_a(i)
            dist.append(w[x] + h[i])
    return max(dist)


print(solution())
