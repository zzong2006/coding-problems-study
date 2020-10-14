import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    board = list(map(int, get_input().strip().split()))
    count = 0
    head = 0
    tail = 0
    total_sum = 0
    while head < n:
        total_sum += board[head]
        head += 1
        while total_sum > k:
            total_sum -= board[tail]
            tail += 1
        if total_sum == k:
            count += 1
    return count


print(solution())
