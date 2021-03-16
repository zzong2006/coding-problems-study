import sys
from collections import deque


class MunJi:
    def __init__(self, y, x, val):
        self.y = y
        self.x = x
        self.val = val


def solution():
    get_input = sys.stdin.readline
    r, c, t = list(get_input().split().strip())
    board = []
    air_cond = []
    que = deque()
    for i in range(r):
        ls = list(get_input().split())
        board.append(ls)
        for j in range(c):
            if board[i][j] > 0:
                que.append((i, j, board[i][j]))
            elif board[i][j] < 0:
                air_cond.append((i, j))


solution()
