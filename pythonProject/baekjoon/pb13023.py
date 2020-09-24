from collections import deque
import sys


def solution(graph, n):
    stack = []

    for i in range(n):
        for k in graph[i]:
            nv = set()
            nv.add(i)
            nv.add(k)

            stack.append([k, 1, nv])
            while stack:
                curr, count, visi = stack.pop()
                if count >= 4:
                    return 1

                for j in graph[curr]:
                    if j not in visi:
                        new_visited = visi.copy()
                        new_visited.add(j)
                        stack.append([j, count + 1, new_visited])
    return 0


get_input = sys.stdin.readline

n, m = list(map(int, get_input().split()))

graph = [set() for _ in range(n)]

for i in range(m):
    a, b = list(map(int, get_input().split()))
    graph[a].add(b)
    graph[b].add(a)

print(solution(graph, n))
