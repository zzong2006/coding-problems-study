import sys


def solution():
    get_input = sys.stdin.readline

    t = int(get_input().strip())

    for i in range(t):
        n, k = list(map(int, get_input().strip().split()))
        board = list(map(int, get_input().strip().split()))

        board.sort()
        mb = board[0]
        total = 0
        for j in range(1, n):
            total += (k - board[j]) // mb

        print(total)


solution()
