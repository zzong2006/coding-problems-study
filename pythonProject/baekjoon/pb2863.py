import sys
import heapq
from collections import deque


def solution():
    get_input = sys.stdin.readline
    a, b = list(map(int, get_input().split()))
    c, d = list(map(int, get_input().split()))

    ans = 0
    val = a/c + b/d

    for i in range(1, 4):
        if i == 1:
            new_val = c/d + a/b
        elif i == 2:
            new_val = d/b + c/a
        elif i == 3:
            new_val = b/a + d/c
        # print(val, new_val)
        if val < new_val:
            ans = i
            val = new_val
    return ans

print(solution())
