import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = []
    for i in range(n):
        board.append(int(get_input().strip()))
    board.sort(reverse=True)
    best = 0
    for i in range(1, n + 1):
        best = max(board[i - 1] * i, best)
    return best

print(solution())

