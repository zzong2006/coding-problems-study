import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    board = list(map(int, get_input().strip().split()))
    shortest = sys.maxsize
    head = 0
    tail = 0
    total_sum = 0
    while head < n:
        total_sum += board[head]
        head += 1
        while total_sum >= k:
            shortest = min(shortest, head - tail)
            total_sum -= board[tail]
            tail += 1

    if shortest == sys.maxsize:
        return 0
    else:
        return shortest


print(solution())
