from collections import deque
import sys

sys.setrecursionlimit(10**7)


def solution(n, path, order):
    def find_circular(i_a, i_b, i_c, curr_k):
        i_a.remove(curr_k)
        i_b.add(curr_k)
        for w in graph[curr_k]:
            if w in i_b:
                return True
            elif w in i_a:
                out = find_circular(i_a, i_b, i_c, w)
                if out:
                    return True
        i_b.remove(curr_k)
        i_c.add(curr_k)
        return False

    answer = True
    path.sort(key=lambda x: (x[0], x[1]))
    graph = [[] for _ in range(n)]

    # make undirected graph
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    # create directed graph based on undirected graph
    visited = {0}
    temp_graph = [[] for _ in range(n)]

    que = deque([0])
    while que:
        k = que.popleft()
        for i in graph[k]:
            if i not in visited:
                temp_graph[k].append(i)
                visited.add(i)
                que.append(i)

    graph = temp_graph

    # order
    for a, b in order:
        if b not in graph[a]:
            graph[a].append(b)
    # find circular
    a = set(range(n))
    b = set()
    c = set()
    for k in range(n):
        if k in a:
            output = find_circular(a, b, c, k)
            if output:
                answer = False
                break

    return answer


print(
    solution(
        9,
        [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
        [[8, 5], [6, 7], [4, 1]],
    )
)
# print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
# print(solution(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[2, 1]]))
