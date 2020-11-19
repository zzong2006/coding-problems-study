import sys

sys.setrecursionlimit(10 ** 7)


def solution():
    """
    LCA 2 solution

    :return:
    """

    def dfs(grp, curr, visited):
        for ed in graph[curr]:
            if len(grp[ed]) < 1:
                grp[ed].append(curr)
                dfs(grp, ed, visited)

    get_input = sys.stdin.readline
    n = int(get_input())
    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = list(map(int, get_input().strip().split()))
        graph[a].append(b)
        graph[b].append(a)
    # make new_graph
    new_graph = [[] for _ in range(n + 1)]
    dfs(new_graph, 1, {1})
    # print(new_graph)

    t = int(get_input())
    # print(new_graph)
    memoization = dict()
    for i in range(t):
        a, b = list(map(int, get_input().strip().split()))
        for k in [a, b]:
            if k not in memoization:
                path = [k]
                curr = k
                while curr != 1:
                    curr = new_graph[curr][-1]
                    path.append(curr)
                memoization[k] = path
        if len(memoization[a]) > len(memoization[b]):
            sh = memoization[b]
            lo = memoization[a]
        else:
            lo = memoization[b]
            sh = memoization[a]
        idx = abs(len(memoization[a]) - len(memoization[b]))

        for k in range(min(len(memoization[a]), len(memoization[b]))):
            if lo[k + idx] == sh[k]:
                print(sh[k])
                break
        # print(memoization[a], memoization[b])


solution()
