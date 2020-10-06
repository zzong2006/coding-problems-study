import sys


def solution():
    get_input = sys.stdin.readline

    n, m = list(map(int, get_input().split()))
    trunks = list(map(int, get_input().split()))

    start = 0
    end = max(trunks)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in trunks:
            if mid < i:
                total += (i - mid)
        # print('start {} end {} mid {} total {}'.format(start, end, mid, total))
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid
    print(ans)


solution()