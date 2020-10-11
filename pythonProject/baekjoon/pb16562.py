import sys
from collections import deque
from itertools import combinations


def solution():
    def find(k):
        q = ls[k]
        if q != k:
            w = find(q)
            ls[k] = w
        return ls[k]

    def union(a, b):
        x = find(a)
        y = find(b)
        if x != y:
            if chin_gu[x] >= chin_gu[y]:
                ls[x] = y
            else:
                ls[y] = x

    get_input = sys.stdin.readline
    n, m, k = list(map(int, get_input().split()))
    chin_gu = list(map(int, get_input().split()))
    ls = list(range(n))
    for i in range(m):
        o, p = list(map(int, get_input().split()))
        union(o - 1, p - 1)

    visited = set()
    total = 0
    for i in range(n):
        x = find(i)
        if x not in visited:
            visited.add(x)
            total += chin_gu[x]
    if total <= k:
        print(total)
    else:
        print("Oh no")
    # print(ls)

solution()
# print(solution())
