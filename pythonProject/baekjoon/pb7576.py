from collections import deque
import sys

get_input = sys.stdin.readline

m, n = list(map(int, get_input().split()))
board = []
for i in range(n):
    board.append(list(map(int, get_input().split())))

que = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            que.append((i, j))

days = 0
seeds = deque()

while True:
    while len(que) > 0:
        y, x = que.popleft()
        for add_x, add_y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_x = x + add_x
            new_y = y + add_y
            if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == 0:
                seeds.append((new_y, new_x))
                board[new_y][new_x] = 1

    if len(seeds) <= 0:
        break
    else:
        days += 1
        que = seeds.copy()
        seeds.clear()


# check all
not_ik = False
for t in board:
    if 0 in t:
        not_ik = True
        break

if not not_ik:
    print(days)
else:
    print(-1)
