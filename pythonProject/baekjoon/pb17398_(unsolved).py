import sys
from collections import deque, defaultdict, Counter
from itertools import permutations
import heapq


def solution():
    def find(x):
        k = ls[x]
        if k != x:
            w = find(k)
            ls[x] = w
            return ls[x]
        else:
            return k

    def union(x, y):
        w = find(x)
        q = find(y)
        if w != q:
            ls[x] = q

    get_input = sys.stdin.readline
    n, m, q = list(map(int, get_input().strip().split()))
    ls = list(range(n))
    link = []
    for i in range(m):
        a, b = list(map(int, get_input().strip().split()))
        link.append((a - 1, b - 1))

    st = []
    for i in range(q):
        t = int(get_input().strip())
        st.append(t - 1)
    cnt = Counter(st)
    how_many = [1] * n
    for i in range(m):
        if cnt[i] == 0:
            a, b = link[i]
            p_a = find(a)
            p_b = find(b)
            union(a, b)
            how_many[p_b] += how_many[p_a]
    answer = 0

    while st:
        idx = st.pop()
        a, b = link[idx]
        p_a = find(a)
        p_b = find(b)
        if p_a != p_b:
            answer += how_many[p_b] * how_many[p_b]
            how_many[p_b] += how_many[p_a]
            union(a, b)

    print(answer)


solution()
