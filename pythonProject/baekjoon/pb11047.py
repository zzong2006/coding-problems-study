import sys
from functools import cmp_to_key
import bisect
import heapq


# Hint. multiset


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    coins = [int(get_input().strip()) for _ in range(n)]

    coins.sort(reverse=True)
    answer = 0
    for c in coins:
        if k // c > 0:
            answer += k // c
            k %= c
        if k == 0:
            break
    print(answer)


solution()
