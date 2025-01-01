import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())

    board = [list(map(int, get_input().strip().split())) for _ in range(n)]
    board.sort(key=lambda x: (x[0], x[1]))
    clock = []

    for i in range(n):
        st, en = board[i]
        if not clock:
            heapq.heappush(clock, en)
        else:
            if clock[0] <= st:
                heapq.heapreplace(clock, en)
            else:
                heapq.heappush(clock, en)
    # print(clock)
    count = len(clock)
    return count


print(solution())
