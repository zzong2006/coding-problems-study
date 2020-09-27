import heapq
import sys
from collections import deque
from typing import List


def get_distance(bd, start, end, size):
    n = len(bd)
    memoization = [[False] * n for i in range(n)]
    memoization[start[0]][start[1]] = True
    que = []
    heapq.heapify(que)
    heapq.heappush(que, [0, start])
    goal_y, goal_x = end

    while que:
        [count, st] = heapq.heappop(que)
        y, x = st
        if y == goal_y and x == goal_x :
            return count

        for add_y, add_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y = y + add_y
            new_x = x + add_x

            if 0 <= new_y < n and 0 <= new_x < n and bd[new_y][new_x] <= size and \
                    memoization[new_y][new_x] is False:
                memoization[new_y][new_x] = True
                heapq.heappush(que, [count + 1, (new_y, new_x)])

    if memoization[goal_y][goal_x] is False:
        return -1
    else:
        return memoization[goal_y][goal_x]


def solution():
    get_input = sys.stdin.readline
    a = int(get_input().strip())
    board = []
    for i in range(a):
        board.append(list(map(int, get_input().strip().split())))
    fish = []

    baby_shark = None
    size = 2
    eat_count = 0
    for i in range(a):
        for j in range(a):
            if board[i][j] != 0 and board[i][j] != 9:
                fish.append([(i, j), board[i][j]])
            if board[i][j] == 9:
                baby_shark = (i, j)
                board[i][j] = 0
    time = 0
    while fish:
        # get distance
        fish_rank = []

        for idx, [f_loc, f_size] in enumerate(fish):
            if f_size < size:
                dist = get_distance(board, baby_shark, f_loc, size)
                if dist != -1:
                    fish_rank.append([dist, f_loc[0], f_loc[1], idx])
        if fish_rank:       # 가장 가까운 물고기 (dist low), 가장 위에 있는 물고기 (y low), 가장 왼쪽에 있는 물고기 (x low)
            fish_rank.sort(key=lambda z: (z[0], z[1], z[2]))
            # print(fish_rank)
            dist, y, x, idx = fish_rank[0]
            baby_shark = (y, x)
            time += dist
            eat_count += 1
            if eat_count == size:
                size += 1
                eat_count = 0
            fish.pop(idx)
        else:
            break
    return time


print(solution())
