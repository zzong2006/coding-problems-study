import sys
import heapq
from collections import deque
import bisect


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().split()))

    ls = [board[0]]

    for i in range(n):
        idx = bisect.bisect_left(ls, board[i])
        if idx >= len(ls):
            ls.append(board[i])
        else:
            ls[idx] = board[i]
        # print(ls)
    return len(ls)


print(solution())
