import sys
from collections import deque, defaultdict
import heapq


def solution():
    get_input = sys.stdin.readline

    case = 1
    while True:
        l, p, v = list(map(int, get_input().strip().split()))
        if l == p == v == 0:
            return
        else:
            answer = min(v % p, l)
            answer += (v // p) * l
            print('Case {}: {}'.format(case, answer))

        case += 1

solution()
