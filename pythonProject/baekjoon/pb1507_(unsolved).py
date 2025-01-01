import sys


def solution():
    get_input = sys.stdin.readline
    t = int(get_input().strip())
    board = []
    for i in range(t):
        board.append(list(map(int, get_input().strip().split())))

    for k in range(t):
        for i in range(t):
            for j in range(t):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])

    for i in range(t):
        for j in range(t):
            print(board[i][j], end=" ")
        print()


solution()
