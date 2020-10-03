import sys
import heapq
from collections import deque


def solution():
    def find_block():
        que = deque()
        final_set = set()
        cnt = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                num = board[i][j]
                if num <= board[i - 1][j] and num <= board[i][j - 1] \
                        and num <= board[i][j + 1] and num <= board[i + 1][j] and (i, j) not in final_set:
                    temp_set = set()
                    que.append((i, j))
                    temp_set.add((i, j))
                    min_val = 10
                    while que:
                        y, x = que.pop()
                        num = board[y][x]
                        for add_y, add_x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                            new_y = y + add_y
                            new_x = x + add_x
                            if 0 <= new_y < n and 0 <= new_x < m and (new_y, new_x) not in temp_set:
                                if num == board[new_y][new_x] :
                                    if new_y == 0 or new_y == n - 1 or new_x == m - 1 or new_x == 0:
                                        que.clear()
                                        temp_set.clear()
                                        break
                                    else:
                                        temp_set.add((new_y, new_x))
                                        que.append((new_y, new_x))
                                elif num < board[new_y][new_x] :
                                    min_val = min(min_val, board[new_y][new_x])
                                else:
                                    que.clear()
                                    temp_set.clear()
                                    break
                    if temp_set:
                        final_set |= temp_set
                        for y, x in temp_set:
                            cnt += (min_val - board[y][x])
                            board[y][x] = min_val
                        # for z in range(n):
                        #     print(board[z][:])
                        # print()
        return cnt

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().split()))
    board = [[0] * m for _ in range(n)]
    for i in range(n):
        st = get_input().strip()
        for j in range(m):
            board[i][j] = int(st[j])

    # board = [list(map(int, get_input().split())) for _ in range(n)]
    found = find_block()
    count = found
    while found:
        found = find_block()
        count += found

    return count


print(solution())
