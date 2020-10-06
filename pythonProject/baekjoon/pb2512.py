import sys


def solution():
    get_input = sys.stdin.readline

    n = list(map(int, get_input().split()))[0]
    board = list(map(int, get_input().split()))
    m = list(map(int, get_input().split()))[0]

    start = 0
    end = m
    ans = 0
    if sum(board) <= m:
        ans = max(board)
    else:
        while start <= end:
            mid = (start + end) // 2
            total = m

            for i in board:
                if i > mid:
                    total -= mid
                else:
                    total -= i
            # print('start {} end {} mid {} total {}'.format(start, end, mid, total))

            if total < 0:
                end = mid - 1
            else:
                start = mid + 1
                ans = mid

    return ans


print(solution())
