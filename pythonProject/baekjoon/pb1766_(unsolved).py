import sys
import heapq


def solution():
    def dfs(curr):
        if curr not in visited:
            visited.add(curr)
            while ls[curr]:
                pop_i = -1 * heapq.heappop(ls[curr])
                dfs(pop_i)
            stack.append(curr)

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    ls = [list() for _ in range(n + 1)]
    for i in range(m):
        a, b = list(map(int, get_input().strip().split()))
        heapq.heappush(ls[a], -b)
    visited = set()
    stack = []
    for i in reversed(range(1, n + 1)):
        if ls[i]:
            dfs(i)
        else:
            if i not in visited:
                stack.append(i)

    while stack:
        i = stack.pop()
        print(i, end=" ")


solution()
