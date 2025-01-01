import sys

# 0-1 bfs problem
from collections import deque


def solution():
    get_input = sys.stdin.readline

    n, m = list(map(int, get_input().strip().split()))
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))

    # marking c
    que = deque()
    c_que = deque()
    que.append((0, 0))
    while len(que) > 0:
        pos = que.popleft()
        y, x = pos

        for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            new_y = y + add_y
            new_x = x + add_x

            if 0 <= new_x < m and 0 <= new_y < n:
                if board[new_y][new_x] == 0:
                    que.append((new_y, new_x))
                    board[new_y][new_x] = 2
                elif board[new_y][new_x] == 1:
                    board[new_y][new_x] = 3
                    c_que.append((new_y, new_x))

    days = 0
    cheese = [len(c_que)]
    while len(c_que) > 0:
        for i in range(len(c_que)):
            pos = c_que.popleft()
            y, x = pos
            board[y][x] = 2

            for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                new_y = y + add_y
                new_x = x + add_x

                if 0 <= new_x < m and 0 <= new_y < n:
                    if board[new_y][new_x] == 1:
                        board[new_y][new_x] = 3
                        c_que.append((new_y, new_x))
                    if board[new_y][new_x] == 0:
                        que.append((new_y, new_x))

        while len(que) > 0:
            pos = que.popleft()
            y, x = pos

            for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                new_y = y + add_y
                new_x = x + add_x

                if 0 <= new_x < m and 0 <= new_y < n:
                    if board[new_y][new_x] == 0:
                        que.append((new_y, new_x))
                        board[new_y][new_x] = 2
                    elif board[new_y][new_x] == 1:
                        board[new_y][new_x] = 3
                        c_que.append((new_y, new_x))
        days += 1
        cheese.append(len(c_que))

    print(days)
    if len(cheese) > 1:
        print(cheese[-2])
    else:
        print(cheese)


solution()
