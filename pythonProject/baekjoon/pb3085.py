import sys

get_input = sys.stdin.readline

N = int(get_input())


def search_longest_color(board, i, j, t) -> int:
    count = 1
    result = 0
    if t == 0:
        A = board[i][0]
        for k in range(1, N):
            if A == board[i][k]:
                count += 1
            else:
                result = max(count, result)
                count = 1
                A = board[i][k]
    if t == 1:
        A = board[0][j]
        for k in range(1, N):
            if A == board[k][j]:
                count += 1
            else:
                result = max(count, result)
                count = 1
                A = board[k][j]

    result = max(count, result)
    return result


board = []
for i in range(N):
    board.append([])
    for j in get_input().strip():
        board[i].append(j)

answer = 0

for i in range(N):
    answer = max(search_longest_color(board, i, j, 0), answer)
for j in range(N):
    answer = max(search_longest_color(board, i, j, 1), answer)

for i in range(N):
    for j in range(N):
        for y, x in [(0, 1), (1, 0)]:
            new_i = i + y  # 바꿀 위치
            new_j = j + x
            if 0 <= new_i < N and 0 <= new_j < N and board[i][j] != board[new_i][new_j]:
                # swap
                temp = board[i][j]
                board[i][j] = board[new_i][new_j]
                board[new_i][new_j] = temp
                # 바꾼 부분 주위 검사
                if x == 1:  # 가로로 치환 일땐 ㅣ ㅣ - 이런식
                    max_count = 0
                    max_count = search_longest_color(board, i, j, 0)
                    max_count = max(max_count, search_longest_color(board, i, j, 1))
                    max_count = max(
                        max_count, search_longest_color(board, new_i, new_j, 1)
                    )
                else:  # 세로로 치환 일땐  =ㅑ= 이런식
                    max_count = 0
                    max_count = search_longest_color(board, i, j, 1)
                    max_count = max(max_count, search_longest_color(board, i, j, 0))
                    max_count = max(
                        max_count, search_longest_color(board, new_i, new_j, 0)
                    )
                answer = max(max_count, answer)

                # 다시 돌려놔야함
                temp = board[i][j]
                board[i][j] = board[new_i][new_j]
                board[new_i][new_j] = temp
print(answer)
