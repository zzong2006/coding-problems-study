import sys
import bisect


def solution():
    get_input = sys.stdin.readline

    t = int(get_input().strip())

    for i in range(t):
        n, large_t = list(map(int, get_input().strip().split()))
        board = list(map(int, get_input().strip().split()))

        sorted_board = sorted(board)
        idx = sorted(range(n), key=lambda k: board[k])

        standard = large_t / 2
        a = bisect.bisect_left(sorted_board, standard)
        b = bisect.bisect_right(sorted_board, standard, lo=a)

        mid = (a + b) // 2

        result = [1] * n
        for j in range(mid, n):
            result[j] = 0

        sorted_result = [x for _, x in sorted(zip(idx, result))]

        for j in range(n):
            print(sorted_result[j], end=" ")
        print()
solution()
