import sys
from collections import deque
from typing import List
sys.setrecursionlimit(10**7)

get_input = sys.stdin.readline


def recur(board_re, ball: tuple, count: int, move: int, direction: tuple, ans: List[int], goal, n, m):
    if goal == move:
        ans.append(count)
        return
    else:
        y, x = ball
        add_y, add_x = direction
        new_y = y + add_y
        new_x = x + add_x

        if 0 <= new_y < n and 0 <= new_x < m and board_re[new_y][new_x] == '.':
            board_re[new_y][new_x] = '?'
            recur(board_re, (new_y, new_x), count, move + 1, direction, ans, goal, n, m)
            board_re[new_y][new_x] = '.'
        else:
            dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            dirs.remove(direction)
            for add_y, add_x in dirs:
                new_y = y + add_y
                new_x = x + add_x
                if 0 <= new_y < n and 0 <= new_x < m and board_re[new_y][new_x] == '.':
                    board_re[new_y][new_x] = '?'
                    recur(board_re, (new_y, new_x), count + 1, move + 1, (add_y, add_x), ans, goal, n, m)
                    board_re[new_y][new_x] = '.'

curr = 0
while True:
    curr += 1
    ip = get_input().strip()
    if ip == "":
        break
    else:
        n, m = list(map(int, ip.split()))
        board = [[0] * m for _ in range(n)]
        start = []
        goal_cnt = 0
        for i in range(n):
            a = get_input().strip()
            for j in range(m):
                board[i][j] = a[j]
                if board[i][j] == '.':
                    start.append((i, j))
                    goal_cnt += 1
        answer = []
        for ball in start:
            y, x = ball
            for dirs in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                add_y, add_x = dirs
                new_y = y + add_y
                new_x = x + add_x
                if 0 <= new_y < n and 0 <= new_x < m and board[new_y][new_x] != '*':
                    board[y][x] = '?'
                    recur(board, ball, 1, 1, dirs, answer, goal_cnt, n, m)
                    board[y][x] = '.'

        if answer:
            print('Case {}: {}'.format(curr, min(answer)))
        else:
            if goal_cnt != 1:
                print('Case {}: {}'.format(curr, -1))
            else:
                print('Case {}: {}'.format(curr, 0))