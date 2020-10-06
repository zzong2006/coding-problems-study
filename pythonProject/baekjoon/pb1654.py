import sys


sys.setrecursionlimit(10**7)

def solution():
    def half_search(prev, curr, found):
        mid = (prev + curr) // 2
        if prev > curr:
            return mid
        total = 0

        for j in board:
            total += (j // mid)
        # print('prev : {}, curr : {}, total : {}'.format(prev, curr, total))
        if total >= k:
            # found = True
            # return half_search(curr, curr * 2, found)
            return half_search(mid + 1, curr, found)
        else:
            return half_search(prev, mid - 1, found)
            # if found:
            #     return curr - 1
            # else:
            #     pass

    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    board = []
    for i in range(n):
        board.append(int(get_input().strip()))
    v = max(board)
    answer = half_search(1, v, False)
    print(answer)


solution()
