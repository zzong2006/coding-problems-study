# 줄 세우기
"""
위상 정렬
"""
import sys


def solution():
    def dfs(c, st):
        for z in board[c]:
            if z not in visited:
                visited.add(z)
                q = dfs(z, st)
                st.append(q)
        return c

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().split()))
    board: list = [list() for i in range(n + 1)]
    for i in range(m):
        a, b = list(map(int, get_input().split()))
        board[a].append(b)
    visited = set()
    stack = []
    for i in range(1, n + 1):
        if i not in visited:
            visited.add(i)
            f = dfs(i, stack)
            stack.append(f)
    for i in reversed(stack):
        print(i, end=" ")


solution()
