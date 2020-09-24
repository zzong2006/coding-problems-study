import sys

sys.setrecursionlimit(10 ** 7)


def solution(board, n, m):
    dp = [[sys.maxsize] * m for _ in range(n)]
    dp[0][0] = 1
    visited = set()
    visited.add((0, 0))
    dfs(board, (0, 0), 1, True, n, m, dp, visited)
    if dp[n - 1][m - 1] == sys.maxsize:
        return -1
    else:
        return dp[n - 1][m - 1]


def dfs(bd, pos, count, can_break, n, m, dp, visit):
    y, x = pos

    if y == n - 1 and x == m - 1:
        dp[n - 1][m - 1] = count
        return
    else:
        for add_y, add_x in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            new_y = y + add_y
            new_x = x + add_x
            new_pos = (new_y, new_x)

            if 0 <= new_y < n and 0 <= new_x < m and new_pos not in visit and dp[new_y][new_x] > count + 1:
                if can_break:
                    if bd[new_y][new_x] == 1:
                        visit.add(new_pos)
                        dp[new_y][new_x] = count + 1
                        dfs(bd, new_pos, count + 1, False, n, m, dp, visit)
                        visit.remove(new_pos)
                    else:
                        visit.add(new_pos)
                        dp[new_y][new_x] = count + 1
                        dfs(bd, new_pos, count + 1, True, n, m, dp, visit)
                        visit.remove(new_pos)
                else:
                    if bd[new_y][new_x] == 0:
                        visit.add(new_pos)
                        dp[new_y][new_x] = count + 1
                        dfs(bd, new_pos, count + 1, False, n, m, dp, visit)
                        visit.remove(new_pos)


get_input = sys.stdin.readline

n, m = list(map(int, get_input().split()))

board = [[0] * m for _ in range(n)]
for i in range(n):
    a = get_input().strip()
    for k in range(len(a)):
        board[i][k] = int(a[k])

print(solution(board, n, m))
