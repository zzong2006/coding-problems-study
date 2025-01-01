import sys
import bisect
from collections import deque


def sliding_window_minimum(w, bd):
    di_co = dict()

    for i in range(w):
        num = bd[i]
        if num in di_co:
            di_co[num] += 1
        else:
            di_co[num] = 1

    for i in range(1, len(bd) - w + 1):
        new_one = bd[i + w - 1]
        if new_one in di_co:
            di_co[new_one] += 1
        prev = bd[i - 1]
        if prev in di_co:
            di_co[prev] -= 1
            if di_co[prev] <= 0:
                di_co.pop(prev, None)

    if di_co.keys():
        minimum = sys.maxsize

        for k in di_co.keys():
            minimum = min(k, minimum)
        return minimum
    else:
        return -1


def solution():
    get_input = sys.stdin.readline

    t = int(get_input().strip())

    for i in range(t):
        n = int(get_input().strip())
        board = list(map(int, get_input().strip().split()))

        result = []
        for j in range(n):
            val = sliding_window_minimum(j + 1, board)
            result.append(val)

        for j in range(n):
            print(result[j], end=" ")
        print()


solution()
