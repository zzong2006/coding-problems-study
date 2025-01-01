import sys
import heapq
from collections import deque


def solution():
    get_input = sys.stdin.readline
    l, w, h = list(map(int, get_input().split()))
    n = int(get_input().strip())
    ls = [0] * (20 + 1)
    for _ in range(n):
        a, b = list(map(int, get_input().split()))
        ls[a] = b
    mass = l * w * h
    count = 0
    for i in reversed(range(20 + 1)):
        if ls[i]:
            sub_mass = 2 ** (3 * i)
            if sub_mass > mass:
                continue
            else:
                mok = mass // sub_mass
                if mok >= ls[i]:
                    mass = mass - (sub_mass * ls[i])
                    count += ls[i]
                else:
                    mass = mass - (sub_mass * mok)
                    count += mok
        if mass == 0:
            return count
    return -1


print(solution())
