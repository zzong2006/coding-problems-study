import sys
from collections import deque


def solution():
    def get_board(bd):
        que = deque()
        count = 0
        no = len(bd)
        for i in range(no):
            for j in range(no):
                if bd[i][j] != 2:
                    que.append([(i, j), bd[i][j]])
                    bd[i][j] = 2
                    count += 1
                    while que:
                        (y, x), color = que.popleft()

                        for add_y, add_x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            new_y = add_y + y
                            new_x = add_x + x
                            if 0 <= new_x < len(bd) and 0 <= new_y < len(bd) and bd[new_y][new_x] == color:
                                bd[new_y][new_x] = 2
                                que.append([(new_y, new_x), color])
        return count


    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = [[0] * n for _ in range(n)]

    for i in range(n):
        b = get_input().strip()
        for j in range(n):
            board[i][j] = b[j]

    copied_board = [board[i][:] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if copied_board[i][j] == 'R':
                copied_board[i][j] = 'G'

    print(get_board(board), get_board(copied_board))

solution()