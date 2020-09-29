import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    board = [[None] * m for _ in range(n)]
    sheep = set()
    wolf = set()
    for i in range(n):
        ls = get_input().strip()
        for j in range(m):
            board[i][j] = ls[j]
            if ls[j] == 'v':
                wolf.add((i, j))
            elif ls[j] == 'o':
                sheep.add((i, j))

    total_sheep = 0
    total_wolf = 0

    visited_sheep = set()
    visited_wolf = set()

    while len(sheep) > 0:
        random_sheep = sheep.pop()
        if random_sheep not in visited_sheep:
            que = deque()
            que.append(random_sheep)
            curr_sheep = 0
            curr_wolf = 0
            while len(que) > 0:
                y, x = que.popleft()
                if board[y][x] != '2':
                    if board[y][x] == 'v':
                        curr_wolf += 1
                        visited_wolf.add((y, x))
                    elif board[y][x] == 'o':
                        curr_sheep += 1
                        visited_sheep.add((y, x))
                    board[y][x] = '2'
                    for add_y, add_x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        new_y = y + add_y
                        new_x = x + add_x
                        if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] != '2' \
                                and board[new_y][new_x] != '#':
                            que.append((new_y, new_x))

            if curr_sheep > curr_wolf:
                total_sheep += curr_sheep
            else:
                total_wolf += curr_wolf
    for wf in wolf:
        if wf not in visited_wolf:
            total_wolf += 1

    print(total_sheep, total_wolf)

solution()