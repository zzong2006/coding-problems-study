import heapq
import sys


def solution():
    get_input = sys.stdin.readline

    possible = int(get_input().strip())

    m, n = list(map(int, get_input().strip().split()))

    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))

    stack = []
    heapq.heapify(stack)

    heapq.heappush(stack, [0, (0, 0), possible])
    memoization = [[[sys.maxsize] * (possible + 1) for _ in range(m)] for _ in range(n)]
    for i in range(possible + 1):
        memoization[0][0][i] = 0

    while stack:
        count, pos, k = heapq.heappop(stack)
        y, x = pos
        if not(x == m - 1 and y == n - 1):
            if k > 0:
                for add_y, add_x in [(-1, -2), (-2, -1), (1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2)]:
                    new_y = y + add_y
                    new_x = x + add_x
                    new_pos = (new_y, new_x)
                    if 0 <= new_y < n and 0 <= new_x < m and board[new_y][new_x] == 0 \
                            and memoization[new_y][new_x][k - 1] > count + 1:
                        memoization[new_y][new_x][k - 1] = count + 1
                        heapq.heappush(stack, [count + 1, new_pos, k - 1])

            for add_y, add_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                new_y = y + add_y
                new_x = x + add_x
                new_pos = (new_y, new_x)
                if 0 <= new_y < n and 0 <= new_x < m and board[new_y][new_x] == 0 \
                        and memoization[new_y][new_x][k] > count + 1:
                    memoization[new_y][new_x][k] = count + 1
                    heapq.heappush(stack, [count + 1, new_pos, k])
        else:
            return memoization[n - 1][m - 1][k]
    if min(memoization[n - 1][m - 1]) == sys.maxsize :
        return -1
    else:
        return min(memoization[n - 1][m - 1])



print(solution())

from itertools import count

for i in count(10, step = 2):
    print(i)