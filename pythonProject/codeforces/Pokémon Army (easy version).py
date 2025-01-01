import sys


# find local minima and maxima


def solution():
    get_input = sys.stdin.readline

    t = int(get_input().strip())

    for i in range(t):
        n, q = list(map(int, get_input().strip().split()))
        board = list(map(int, get_input().strip().split()))
        total = 0
        prev = 0
        find_max = True
        # q is always 0
        if n == 1:
            print(board[0])
            continue
        for k in range(n):
            if find_max:
                if k == 0:
                    if board[k] >= board[k + 1]:
                        total += board[k]
                        find_max = False
                elif k == n - 1:
                    if board[k - 1] <= board[k]:
                        total += board[k]
                else:
                    if board[k - 1] <= board[k] and board[k] >= board[k + 1]:
                        total += board[k]
                        find_max = False
            else:
                if k == n - 1:
                    if board[k - 1] <= board[k]:
                        total -= board[k]
                else:
                    if board[k - 1] >= board[k] and board[k] <= board[k + 1]:
                        total -= board[k]
                        find_max = True
        print(total)


solution()
