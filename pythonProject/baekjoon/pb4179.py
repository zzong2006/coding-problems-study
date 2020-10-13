from collections import deque
from itertools import combinations
import sys


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    board = [[0] * m for _ in range(n)]
    fire = [[0] * m for _ in range(n)]

    location = None
    fire_loc = None
    que = deque()
    for i in range(n):
        ls = get_input().strip()
        for j in range(m):
            board[i][j] = ls[j]
            fire[i][j] = ls[j]
            if ls[j] == 'J':
                location = (i, j)
                board[i][j] = 0
                fire[i][j] = '.'
            if ls[j] == 'F':
                fire_loc = (i, j)
                fire[i][j] = 0
                que.append([(i, j), 0])
                board[i][j] = '#'

    memo = [[sys.maxsize for _ in range(n)]]
    # 일단 불을 지르자
    while que:
        (y, x), d = que.popleft()
        for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            new_y = y + add_y
            new_x = x + add_x
            if 0 <= new_y < n and 0 <= new_x < m and fire[new_y][new_x] != '#' and \
                    (fire[new_y][new_x] == '.' or fire[new_y][new_x] > d + 1):
                fire[new_y][new_x] = d + 1
                que.append([(new_y, new_x), d + 1])
    # for ii in range(n):
    #     print(fire[ii][:])
    # for ii in range(n):
    #     print(board[ii][:])

    que.clear()
    que.append([location, 0])
    # 그리고 도망치자
    while que:
        (y, x), d = que.popleft()

        for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            new_y = y + add_y
            new_x = x + add_x
            if 0 <= new_y < n and 0 <= new_x < m and board[new_y][new_x] != '#' and board[new_y][new_x] != 'F' and \
                    (fire[new_y][new_x] == '.' or fire[new_y][new_x] > d + 1) \
                    and (board[new_y][new_x] == '.' or board[new_y][new_x] > d + 1):
                board[new_y][new_x] = d + 1
                que.append([(new_y, new_x), d + 1])
    # for ii in range(n):
    #     print(board[ii][:])
    # 가장자리 검사
    answer = sys.maxsize
    for i in range(m):
        if board[0][i] != '#' and board[0][i] != '.':
            answer = min(answer, board[0][i])
        if board[n - 1][i] != '#' and board[n - 1][i] != '.':
            answer = min(answer, board[n - 1][i])
    for j in range(n):
        if board[j][0] != '#' and board[j][0] != '.':
            answer = min(answer, board[j][0])
        if board[j][m - 1] != '#' and board[j][m - 1] != '.':
            answer = min(answer, board[j][m - 1])
    if answer == sys.maxsize:
        return 'IMPOSSIBLE'
    else:
        return answer + 1

print(solution())
