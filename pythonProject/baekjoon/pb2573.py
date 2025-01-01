import sys
import heapq
from collections import deque


def solution():
    def melt(gla_set):
        melting = [[0] * m for _ in range(n)]

        for i, j in gla_set:
            if board[i][j] != 0:
                for add_y, add_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    new_y = i + add_y
                    new_x = j + add_x
                    if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == 0:
                        melting[i][j] += 1
        remove_set = set()
        for i, j in gla_set:
            if board[i][j] != 0:
                board[i][j] = max(board[i][j] - melting[i][j], 0)
                if board[i][j] == 0:
                    remove_set.add((i, j))
        gla_set -= remove_set

    def count_zodiac():
        new_board = [board[i_1][:] for i_1 in range(n)]
        que = deque()
        count = 0
        for i in range(n):
            for j in range(m):
                if new_board[i][j] != 0:
                    count += 1
                    que.append((i, j))
                    new_board[i][j] = 0
                    while que:
                        y, x = que.pop()
                        for add_y, add_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            new_y = y + add_y
                            new_x = x + add_x
                            if (
                                0 <= new_x < m
                                and 0 <= new_y < n
                                and new_board[new_y][new_x] != 0
                            ):
                                new_board[new_y][new_x] = 0
                                que.append((new_y, new_x))
        return count

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().split()))
    board = [list(map(int, get_input().split())) for _ in range(n)]
    glacial_set = set()

    for i_3 in range(n):
        for j_1 in range(m):
            if board[i_3][j_1] != 0:
                glacial_set.add((i_3, j_1))

    cnt = count_zodiac()
    time = 0
    while cnt < 2 and cnt != 0:
        melt(glacial_set)
        cnt = count_zodiac()
        time += 1
    if cnt == 0:
        return 0
    else:
        return time


print(solution())
