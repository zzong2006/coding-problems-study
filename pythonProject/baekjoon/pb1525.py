import sys
from collections import deque


def solution():
    def check(z):
        ans = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        for k in range(3):
            for h in range(3):
                if z[k][h] != ans[k][h]:
                    return False
        return True

    get_input = sys.stdin.readline
    board = []
    for i in range(3):
        board.append(list(map(int, get_input().strip().split())))

    pos = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                pos = (i, j)
    que = deque()
    que.append([board, pos, 0])
    visited = set()
    while que:
        bd, pos, count = que.popleft()

        if check(bd):
            return count
        else:
            tp = tuple(map(tuple, bd))
            if tp not in visited:
                visited.add(tp)
                y, x = pos
                for add_y, add_x in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                    new_y = y + add_y
                    new_x = x + add_x
                    if 0 <= new_y < 3 and 0 <= new_x < 3:
                        new_board = [row[:] for row in bd]
                        new_board[new_y][new_x], new_board[y][x] = (
                            new_board[y][x],
                            new_board[new_y][new_x],
                        )
                        tp = tuple(map(tuple, new_board))
                        if tp not in visited:
                            que.append([new_board, (new_y, new_x), count + 1])
    return -1


print(solution())
