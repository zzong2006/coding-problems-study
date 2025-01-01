import sys
from collections import deque
from itertools import combinations


def solution():
    get_input = sys.stdin.readline
    n, l, r = list(map(int, get_input().split()))
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().split())))

    count = 0
    found = True
    while found:
        found = False
        visited = set()
        que = deque()
        # new_board = [board[i][:] for i in range(n)]
        count += 1

        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    que.append((i, j))
                    temp_set = set([(i, j)])
                    visited.add((i, j))
                    temp_sum = board[i][j]
                    while que:
                        y, x = que.popleft()
                        for add_y, add_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_y = y + add_y
                            new_x = x + add_x
                            if (
                                0 <= new_y < n
                                and 0 <= new_x < n
                                and (new_y, new_x) not in visited
                                and l <= abs(board[y][x] - board[new_y][new_x]) <= r
                            ):
                                que.append((new_y, new_x))
                                visited.add((new_y, new_x))
                                temp_set.add((new_y, new_x))
                                temp_sum += board[new_y][new_x]
                    # print(temp_set)
                    if len(temp_set) > 1:
                        found = True
                        new_val = temp_sum // len(temp_set)
                        while temp_set:
                            y, x = temp_set.pop()
                            board[y][x] = new_val
        # board = [new_board[i][:] for i in range(n)]
        # for i in range(n):
        #     print(board[i][:])

    return count - 1


print(solution())
