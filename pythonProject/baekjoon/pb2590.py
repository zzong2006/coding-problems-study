import sys
from collections import deque


def solution():
    def place_rectangle(n_b, l, remained):
        for i in range(6 - l + 1):
            for j in range(6 - l + 1):
                if (
                    n_b[i][j] is False
                    and n_b[i][j + l - 1] is False
                    and n_b[i + l - 1][j + l - 1] is False
                    and n_b[i + l - 1][j] is False
                ):
                    remained -= 1
                    for k in range(i, i + l):
                        for z in range(j, j + l):
                            n_b[k][z] = True
                    if remained <= 0:
                        return remained
        return remained

    get_input = sys.stdin.readline
    board = []
    for i in range(6):
        board.append(int(get_input().strip()))

    board_list = []
    for i in reversed(range(5)):
        curr = 0
        while board[i] > 0:
            if not curr < len(board_list):
                board_list.append([[False] * 6 for _ in range(6)])
            else:
                new_board = board_list[curr]
                board[i] = place_rectangle(new_board, i + 1, board[i])

                curr += 1
    return len(board_list) + board[5]


print(solution())
