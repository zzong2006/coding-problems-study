from collections import deque
from sys import maxsize


def solution(board):
    que = deque()
    n, m = len(board), len(board[0])
    # (y, x, dir, val)
    que.append((0, 0, 'r', 0))
    que.append((0, 0, 'd', 0))
    answer = []
    check = [[maxsize] * m for _ in range(n)]

    while len(que) > 0:
        # 0 : right , 1: down , 2 : left, 3 : up
        y, x, direction, val = que.popleft()
        if y == n - 1 and x == m - 1:
            answer.append(val)
        else:
            for add_y, add_x, go in [(0, 1, 'r'), (1, 0, 'd'), (0, -1, 'l'), (-1, 0, 'u')]:
                new_y = y + add_y
                new_x = x + add_x
                if (direction == 'r' and go == 'l') or (direction == 'l' and go == 'r') or (
                        direction == 'u' and go == 'd') or (direction == 'd' and go == 'u'):
                    continue
                elif direction != go:
                    new_val = val + 600
                elif direction == go:
                    new_val = val + 100

                if 0 <= new_x < m and 0 <= new_y < n and board[new_y][new_x] == 0 and (check[new_y][new_x] >= new_val):
                    check[new_y][new_x] = new_val
                    que.append((new_y, new_x, go, new_val))

    return min(answer)


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
#                 [1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
#                 [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))
