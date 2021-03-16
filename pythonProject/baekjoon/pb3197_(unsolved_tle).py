import sys
from collections import deque


def solution():
    def get_round_max(input_board, y, x):
        max_val = 0
        for add_y, add_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_y = add_y + y
            new_x = add_x + x
            if 0 <= new_y < len(input_board) and 0 <= new_x < len(input_board[0]):
                if isinstance(input_board[new_y][new_x], int):
                    max_val = max(max_val, input_board[new_y][new_x])
        return max_val

    def fill_with_number(input_board, new_que):
        max_val = 0
        r, c = len(input_board), len(input_board[0])
        while new_que:
            y, x = new_que.popleft()

            for add_y, add_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y = add_y + y
                new_x = add_x + x

                if 0 <= new_y < r and 0 <= new_x < c:
                    if input_board[new_y][new_x] == 'X':
                        new_que.append((new_y, new_x))
                        input_board[new_y][new_x] = input_board[y][x] + 1
                        max_val = input_board[new_y][new_x]
        return input_board, max_val

    def is_possible(input_board, start_l, end_l, max_val):
        new_que = deque()
        new_que.append(start_l)
        visited = {start_l}
        r, c = len(input_board), len(input_board[0])

        while new_que:
            y, x = new_que.popleft()
            for add_y, add_x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_y = add_y + y
                new_x = add_x + x

                if (new_y, new_x) == end_l:
                    return True
                if 0 <= new_y < r and 0 <= new_x < c and (
                new_y, new_x) not in visited and input_board[new_y][new_x] <= max_val:
                    visited.add((new_y, new_x))
                    new_que.append((new_y, new_x))

        return False

    get_input = sys.stdin.readline
    r, c = list(map(int, get_input().split()))
    board = []
    start = None
    end = None
    ice_queue = deque()

    for i in range(r):
        board.append(list(get_input().strip()))
        for j in range(len(board[i])):
            if board[i][j] == 'L':
                board[i][j] = '.'
                if start is None:
                    start = (i, j)
                else:
                    end = (i, j)
            if board[i][j] == '.':
                ice_queue.append((i, j))
                board[i][j] = 0

    board, end_num = fill_with_number(board, ice_queue)
    start_num = 0
    result = end_num
    while start_num <= end_num:
        mid = (start_num + end_num) // 2
        if is_possible(board, start, end, mid):
            result = mid
            end_num = mid - 1
        else:
            start_num = mid + 1
    print(result)


solution()
