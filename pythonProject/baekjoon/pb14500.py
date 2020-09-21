import sys

get_input = sys.stdin.readline

n, m = list(map(int, get_input().split()))

board = []
for i in range(n):
    board.append(list(map(int, get_input().split())))

answer = 0
# 네모 ㅁ
for i in range(n - 1):
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1])

# ㅡ
for i in range(n):
    for j in range(m - 3):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3])

for i in range(n - 3):
    for j in range(m):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j])

# L (4가지)
for i in range(n - 2):  # ㄴ
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1])

for i in range(n - 1):  #
    for j in range(m - 2):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i][j + 1] + board[i][j + 2])

for i in range(n - 2):  # ㄱ
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1])

for i in range(n - 1):  #
    for j in range(m - 2):
        answer = max(answer, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j + 2])

# 대칭
for i in range(n - 2):  # ㄴ
    for j in range(m - 1):
        answer = max(answer, board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1] + board[i + 2][j])

for i in range(n - 1):  #
    for j in range(m - 2):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 2])

for i in range(n - 2):  # ㄱ
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i][j + 1])

for i in range(n - 1):  #
    for j in range(m - 2):
        answer = max(answer, board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2] + board[i][j])

# ㅗ (4 가지)
for i in range(n - 2):  # ㅓ
    for j in range(m - 1):
        answer = max(answer, board[i + 1][j] + board[i + 1][j + 1] + board[i][j + 1] + board[i + 2][j + 1])

for i in range(n - 2):  # ㅏ
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 1][j + 1])

for i in range(n - 1):  # ㅗ
    for j in range(m - 2):
        answer = max(answer, board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])

for i in range(n - 1):  # ㅜ
    for j in range(m - 2):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])

# ㄴㄱ 모양 (2 가지)
for i in range(n - 1):
    for j in range(m - 2):
        answer = max(answer, board[i + 1][j] + board[i + 1][j + 1] + board[i][j + 1] + board[i][j + 2])

for i in range(n - 2):
    for j in range(m - 1):
        answer = max(answer, board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])
# 대칭
for i in range(n - 1):
    for j in range(m - 2):
        answer = max(answer, board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2])

for i in range(n - 2):
    for j in range(m - 1):
        answer = max(answer, board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j] + board[i + 2][j])

print(answer)
