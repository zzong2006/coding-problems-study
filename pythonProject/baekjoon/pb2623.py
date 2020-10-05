import sys


def solution():
    def dfs(curr):
        decision = True
        if curr in visited:
            return False
        elif curr not in certain:
            visited.add(curr)
            for pop_i in ls[curr]:
                decision &= dfs(pop_i)
                if decision is False:
                    return False
            stack.append(curr)
            visited.remove(curr)
            certain.add(curr)
        return True

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    ls = [list() for _ in range(n + 1)]
    for i in range(m):
        k = list(map(int, get_input().strip().split()))

        for j in range(1, k[0]):
            a, b = k[j], k[j + 1]
            ls[a].append(b)
    visited = set()
    certain = set()
    stack = []

    # sort
    for i in range(1, n + 1):
        if ls[i]:
            res = dfs(i)
            if res is False:
                break
    else:
        for i in range(1, n + 1):
            if i not in certain:
                stack.append(i)

        while stack:
            i = stack.pop()
            print(i, end=" ")
        return
    print(0)


solution()
