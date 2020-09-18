import queue
from sys import maxsize


def solution(n, edge):
    connected = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for x, y in edge:
        connected[x].append(y)
        connected[y].append(x)

    mh = []
    dist = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i] = maxsize

    for i in connected[1]:
        mh.append(i)
        visited[1] = True
        dist[i] = 1
    dist[1] = 0

    while mh:
        a = mh.pop(0)

        for i in connected[a]:
            if not visited[i]:
                visited[i] = True
                mh.append(i)
                dist[i] = min(dist[i], dist[a] + 1)
    max_val = 0
    dist.sort(reverse=True)
    answer = dist.count(dist[0])

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
