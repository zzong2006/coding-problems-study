import sys
import heapq
from collections import deque


def solution():
    get_input = sys.stdin.readline
    idx = 0
    while True:
        idx += 1
        n = int(get_input().strip())
        if n == 0:
            break
        board = [list(map(int, get_input().split())) for _ in range(n)]
        cost = [[float('inf')] * n for _ in range(n)]
        que = []

        heapq.heappush(que, (board[0][0], (0, 0)))
        cost[0][0] = board[0][0]

        while que:
            debt, pos = heapq.heappop(que)
            y, x = pos
            if y == n - 1 and x == n - 1:
                break
            if cost[y][x] < debt:
                continue
            for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_y = y + a
                new_x = x + b
                if 0 <= new_y < n and 0 <= new_x < n and cost[new_y][new_x] > board[new_y][new_x] + debt:
                    cost[new_y][new_x] = board[new_y][new_x] + debt
                    heapq.heappush(que, (cost[new_y][new_x], (new_y, new_x)))
        print('Problem {}: {}'.format(idx, cost[n - 1][n - 1]))
    count = 0
    return count


solution()