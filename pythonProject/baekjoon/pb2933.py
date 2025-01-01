import sys
from collections import deque


def solution():
    def check_all(new_bd, total):
        que = deque()
        for q in reversed(range(n)):
            for w in reversed(range(m)):
                if new_bd[q][w] == "x":
                    new_bd[q][w] = "c"
                    que.append((q, w))
                    ls = []
                    while que:
                        pos = que.popleft()
                        ls.append(pos)
                        y, x = pos

                        for add_y, add_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            new_y = y + add_y
                            new_x = x + add_x
                            if (
                                0 <= new_y < n
                                and 0 <= new_x < m
                                and new_bd[new_y][new_x] == "x"
                            ):
                                new_bd[new_y][new_x] = "c"
                                que.append((new_y, new_x))

                    ls.sort(key=lambda x: (x[0], x[1]), reverse=True)
                    for y, x in ls:
                        if y == n - 1:
                            break
                        elif y < n:
                            return ls

        return []

    def go_down(crystal_list):
        # find gap
        bottom = dict()
        for y, x in crystal_list:
            if x in bottom:
                if bottom[x] < y:
                    bottom[x] = y
            else:
                bottom[x] = y

        max_gap = sys.maxsize
        for k in bottom.keys():
            x, y = k, bottom[k]
            for q in range(y + 1, n):
                if board[q][x] == "x":
                    max_gap = min(max_gap, q - y - 1)
                    break
            else:
                max_gap = min(max_gap, n - y - 1)

        for y, x in crystal_list:
            board[y][x] = "."
            board[y + max_gap][x] = "x"

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    board = [[0] * m for _ in range(n)]
    total_crystal = 0
    for i in range(n):
        st = get_input().strip()
        for j in range(m):
            board[i][j] = st[j]
            if st[j] == "x":
                total_crystal += 1
    t = int(get_input().strip())
    cads = list(map(int, get_input().strip().split()))
    left = True
    for cmd in cads:
        if left:
            for i in range(m):
                if board[n - cmd][i] == "x":
                    board[n - cmd][i] = "."
                    total_crystal -= 1
                    break
            left = False
        else:
            for i in reversed(range(m)):
                if board[n - cmd][i] == "x":
                    board[n - cmd][i] = "."
                    total_crystal -= 1
                    break
            left = True
        new_board = [board[i][:] for i in range(n)]
        crystals = check_all(new_board, total_crystal)
        go_down(crystals)
        while crystals:
            crystals = check_all(new_board, total_crystal)
            go_down(crystals)

    for i in range(n):
        for j in range(m):
            print(board[i][j], end="")
        print()


solution()
