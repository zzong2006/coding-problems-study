import math
import sys
from collections import Counter, defaultdict


def solution():
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            ls[a] = b
            remained[b] += remained[a]
            remained[a] = 0
            remained[b] -= 1

    def find(x):
        k = ls[x]
        if k != ls[x]:
            if remained[x] > 0:
                remained[k] += remained[x]
                remained[x] = 0
            w = find(k)
            if remained[k] > 0:
                remained[w] += remained[k]
                remained[k] = 0
            ls[x] = w
        return ls[x]

    get_input = sys.stdin.readline
    n, l = list(map(int, get_input().strip().split()))
    ls = list(range(l + 1))
    remained = [1] * (l + 1)
    for i in range(n):
        # print('{}'.format(i + 1), end=" ")
        aa, bb = list(map(int, get_input().strip().split()))
        pa = find(aa)
        pb = find(bb)
        # print('parents', ls)
        # print('   tong', remained)
        if remained[pa] > 0:
            union(aa, bb)
            print("LADICA")
            continue
        if remained[pb] > 0:
            union(aa, bb)
            print("LADICA")
            continue

        print("SMECE")


solution()
