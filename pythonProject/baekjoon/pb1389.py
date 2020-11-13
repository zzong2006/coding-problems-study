import sys


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    graph = [[False] * n for _ in range(n)]
    board = [[float('inf')] * n for _ in range(n)]
    for i in range(m):
        a, b = list(map(int, get_input().strip().split()))
        graph[a - 1][b - 1] = True
        graph[b - 1][a - 1] = True
        board[a - 1][b - 1] = 1
        board[b - 1][a - 1] = 1


    for k in range(n):
        for i in range(n):
            for j in range(n):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
                board[j][i] = board[i][j]

    sum_up = []
    for i in range(n):
        # print(board[i][:])
        sum_up.append(sum(board[i]))
    print(sum_up.index(min(sum_up)) + 1)


solution()
