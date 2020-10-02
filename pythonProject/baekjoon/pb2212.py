import sys
from collections import deque, defaultdict
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    k = int(get_input().strip())
    board = list(map(int, get_input().strip().split()))
    board.sort()
    if n <= k:
        return 0
    elif k == 1:
        return board[-1] - board[0]
    else:
        dist = []
        for i in range(n - 1):
            nd = abs(board[i] - board[i + 1])
            heapq.heappush(dist, -nd)
        for i in range(k - 1):
            heapq.heappop(dist)
        hap = 0
        for i in range(len(dist)):
            hap += -(heapq.heappop(dist))
        return hap



print(solution())
