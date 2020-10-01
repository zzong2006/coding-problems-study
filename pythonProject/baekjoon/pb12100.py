import sys
from collections import deque


def move(bd, direction, n):
    already = set()
    if direction == 'u':
        for i in range(1, n):
            for k in range(n):
                if bd[i][k] != 0:
                    for j in reversed(range(i)):
                        if bd[j][k] != 0:
                            break
                    if bd[j][k] != 0:
                        if bd[i][k] == bd[j][k] and (j, k) not in already:
                            already.add((j, k))
                            bd[j][k] += bd[i][k]
                            bd[i][k] = 0
                        else:
                            if j + 1 < n and j + 1 != i:
                                bd[j + 1][k] = bd[i][k]
                                bd[i][k] = 0
                    else:
                        bd[j][k] += bd[i][k]
                        bd[i][k] = 0
    elif direction == 'd':
        for i in reversed(range(n - 1)):
            for k in range(n):
                if bd[i][k] != 0:
                    for j in range(i + 1, n):
                        if bd[j][k] != 0:
                            break
                    if bd[j][k] != 0:
                        if bd[i][k] == bd[j][k] and (j, k) not in already:
                            already.add((j, k))
                            bd[j][k] += bd[i][k]
                            bd[i][k] = 0
                        else:
                            if j - 1 < n and j - 1 != i:
                                bd[j - 1][k] = bd[i][k]
                                bd[i][k] = 0
                    else:
                        bd[j][k] += bd[i][k]
                        bd[i][k] = 0
    elif direction == 'r':
        for i in reversed(range(n - 1)):
            for k in range(n):
                if bd[k][i] != 0:
                    for j in range(i + 1, n):
                        if bd[k][j] != 0:
                            break
                    if bd[k][j] != 0:
                        if bd[k][i] == bd[k][j] and (k, j) not in already:
                            already.add((k, j))
                            bd[k][j] += bd[k][i]
                            bd[k][i] = 0
                        else:
                            if j - 1 < n and j - 1 != i:
                                bd[k][j - 1] = bd[k][i]
                                bd[k][i] = 0
                    else:
                        bd[k][j] += bd[k][i]
                        bd[k][i] = 0
    elif direction == 'l':
        for i in range(1, n):
            for k in range(n):
                if bd[k][i] != 0:
                    for j in reversed(range(i)):
                        if bd[k][j] != 0:
                            break
                    if bd[k][j] != 0:
                        if bd[k][i] == bd[k][j] and (k, j) not in already:
                            already.add((k, j))
                            bd[k][j] += bd[k][i]
                            bd[k][i] = 0
                        else:
                            if j + 1 < n and j + 1 != i:
                                bd[k][j + 1] = bd[k][i]
                                bd[k][i] = 0
                    else:
                        bd[k][j] += bd[k][i]
                        bd[k][i] = 0


def get_maximum_cell(bd, n):
    max_val = 0
    for i in range(n):
        max_val = max(max_val, max(bd[i][:]))
    return max_val


def solution():
    get_input = sys.stdin.readline
    n: int = int(get_input().strip())
    board = [list(map(int, get_input().strip().split())) for _ in range(n)]

    max_val = 0
    que = deque()
    que.append([board, 0])

    while que:
        pan, count = que.popleft()
        if count == 5:
            max_val = max(max_val, get_maximum_cell(pan, n))
        else:
            for d in ['r', 'l', 'd', 'u']:
                new_board = [pan[i][:] for i in range(n)]
                move(new_board, d, n)
                que.append([new_board, count + 1])
    return max_val


print(solution())
