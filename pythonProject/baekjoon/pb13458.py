import sys
import heapq
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().split()))
    b, c = list(map(int, get_input().split()))

    for i in range(n):
        board[i] = max(board[i] - b, 0)
    count = n
    for i in range(n):
        if board[i] != 0:
            if board[i] < c:
                count += 1
            else:
                count += board[i] // c
                if board[i] % c > 0:
                    count += 1
    return count


print(solution())
