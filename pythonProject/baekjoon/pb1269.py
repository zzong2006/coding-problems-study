import sys
from collections import deque
import heapq


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().split()))
    large_a = set(list(map(int, get_input().split())))
    large_b = set(list(map(int, get_input().split())))

    return len(large_b - large_a) + len(large_a - large_b)


print(solution())
