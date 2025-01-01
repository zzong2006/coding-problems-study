import sys

get_input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n = int(get_input().strip())

board = []
for i in range(n):
    board.append(list(map(int, get_input().strip().split())))

dp = [[-1] * n for _ in range(n)]


def recur(pos, count, prev, n, st_pos):
    y, x = pos
    can_move = False
    for add_y, add_x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_y = y + add_y
        new_x = x + add_x
        new_pos = (new_y, new_x)
        if 0 <= new_y < n and 0 <= new_x < n and board[new_y][new_x] > prev:
            if dp[new_y][new_x] == -1:
                can_move = True
                recur(new_pos, count + 1, board[new_y][new_x], n, st_pos)
            else:
                can_move = True
                res_y, res_x = st_pos
                dp[res_y][res_x] = max(dp[res_y][res_x], count + dp[new_y][new_x] + 1)
    if not can_move:
        res_y, res_x = st_pos
        dp[res_y][res_x] = max(dp[res_y][res_x], count)


pos_list = []
for i in range(n):
    for j in range(n):
        pos_list.append((i, j, board[i][j]))

pos_list.sort(key=lambda x: x[2], reverse=True)

for y, x, _ in pos_list:
    st = (y, x)
    recur(st, 0, board[y][x], n, st)

ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans + 1)
