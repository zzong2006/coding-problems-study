import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    t = int(get_input().strip())
    for _ in range(t):
        h, w = list(map(int, get_input().strip().split()))

        board = [[0] * w for i in range(h)]
        start_pos = []
        hogtie = []
        for i in range(h):
            inp = get_input().strip()
            for j in range(w):
                board[i][j] = inp[j]
                if (i == 0 or i == h - 1) and (inp[j] == "#" or inp[j] == "."):
                    start_pos.append((i, j))
                if inp[j] == "$":
                    hogtie.append((i, j))
        print(hogtie, start_pos)
        possible_sum = []
        while start_pos:
            y, x = start_pos.pop()
            que = deque()
            memo = [[[sys.maxsize] * 3 for _ in range(w)] for _ in range(h)]
            if board[y][x] == "#":
                memo[y][x][0] = 1
                que.append([y, x, memo[y][x][0], 0, 0])
            elif board[y][x] == ".":
                memo[y][x][0] = 0
                que.append([y, x, memo[y][x][0], 0, 0])
            elif board[y][x] == "$":
                memo[y][x][1] = 0
                idx = hogtie.index((y, x))
                que.append([y, x, memo[y][x][1], 1, (1 << idx)])

            while que:
                y, x, door, how_many, which = que.popleft()
                if how_many < 2:
                    for add_y, add_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        new_y = y + add_y
                        new_x = x + add_x

                        if (
                            0 <= new_y < h
                            and 0 <= new_x < w
                            and board[new_y][new_x] != "*"
                        ):
                            if (
                                board[new_y][new_x] == "#"
                                and memo[new_y][new_x][how_many] > door + 1
                            ):
                                memo[new_y][new_x][how_many] = door + 1
                                que.append([new_y, new_x, door + 1, how_many, which])
                            elif (
                                board[new_y][new_x] == "."
                                and memo[new_y][new_x][how_many] > door
                            ):
                                memo[new_y][new_x][how_many] = door
                                que.append([new_y, new_x, door, how_many, which])
                            elif board[new_y][new_x] == "$":
                                idx = hogtie.index((new_y, new_x))

                                if (1 << idx) & which != 0 and memo[new_y][new_x][
                                    how_many
                                ] > door:  # 이미 구출한 인질
                                    memo[new_y][new_x][how_many] = door
                                    que.append([new_y, new_x, door, how_many, which])
                                elif (1 << idx) & which == 0 and memo[new_y][new_x][
                                    how_many + 1
                                ] > door:
                                    memo[new_y][new_x][how_many + 1] = door
                                    que.append(
                                        [
                                            new_y,
                                            new_x,
                                            door,
                                            how_many + 1,
                                            which + (1 << idx),
                                        ]
                                    )
            [(y1, x1), (y2, x2)] = hogtie
            possible_sum.append(min(memo[y1][x1][2], memo[y2][x2][2]))
        print(min(possible_sum))


solution()
