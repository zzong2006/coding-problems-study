import heapq
import sys
from collections import deque
from typing import List


def solution():
    def search_all_fish(loc):
        que = deque()
        fs = []  # 먹을 수 있는 고기만 담기
        que.append([loc, 0])
        visited = [[sys.maxsize] * n for _ in range(n)]
        y, x = loc
        visited[y][x] = 0

        while que:
            (y, x), d = que.popleft()

            for add_y, add_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_y = y + add_y
                new_x = x + add_x

                if 0 <= new_y < n and 0 <= new_x < n and board[new_y][new_x] <= baby_size and \
                        visited[new_y][new_x] > d + 1:
                    visited[new_y][new_x] = d + 1
                    que.append([(new_y, new_x), d + 1])

        for ii in range(n):
            for jj in range(n):
                if board[ii][jj] < baby_size and board[ii][jj] != 0 and visited[ii][jj] != sys.maxsize:
                    fs.append((visited[ii][jj], ii, jj))
        fs.sort(key=lambda x: (x[0], x[1], x[2]))
        # print(fs)
        return fs

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        ll = list(map(int, get_input().strip().split()))
        for j in range(n):
            if ll[j] != 9:
                board[i][j] = ll[j]
            else:
                baby = (i, j)
                board[i][j] = 0

    time = 0
    eat_count = 0
    baby_size = 2
    f = [0]
    while f:
        f = search_all_fish(baby)
        if f:
            dd, yy, xx = f[0]
            baby = (yy, xx)
            board[yy][xx] = 0
            time += dd
            eat_count += 1
            if eat_count >= baby_size:
                eat_count = 0
                baby_size += 1

    return time


print(solution())
