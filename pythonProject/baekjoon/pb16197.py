import sys
from typing import List

get_input = sys.stdin.readline


def move_coin(
    first_coin: tuple,
    second_coin: tuple,
    n: int,
    m: int,
    count: int,
    board: list,
    answer: List[int],
    dp: dict,
) -> None:
    f_y, f_x = first_coin
    s_y, s_x = second_coin
    first_coin_dead = False
    second_coin_dead = False
    if count > 10:
        return
    if f_y < 0 or f_x < 0 or f_x >= m or f_y >= n:
        first_coin_dead = True

    if s_y < 0 or s_x < 0 or s_x >= m or s_y >= n:
        second_coin_dead = True

    if first_coin_dead & second_coin_dead is True:
        return
    elif first_coin_dead | second_coin_dead is True:
        # print(first_coin, first_coin_dead, second_coin, second_coin_dead)
        answer.append(count)
    else:
        for add_y, add_x in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
            coin_list = []
            for coin_y, coin_x in [first_coin, second_coin]:
                new_y = coin_y + add_y
                new_x = coin_x + add_x
                if 0 <= new_y < n and 0 <= new_x < m:
                    if board[new_y][new_x] == "." or board[new_y][new_x] == "o":
                        coin_list.append((new_y, new_x))
                    elif board[new_y][new_x] == "#":
                        coin_list.append((coin_y, coin_x))
                else:
                    coin_list.append((new_y, new_x))
            if (coin_list[0], coin_list[1]) in dp:
                if dp[(coin_list[0], coin_list[1])] > count + 1:
                    dp[(coin_list[0], coin_list[1])] = count + 1
                    move_coin(
                        coin_list[0], coin_list[1], n, m, count + 1, board, answer, dp
                    )
            else:
                dp[(coin_list[0], coin_list[1])] = count + 1
                move_coin(
                    coin_list[0], coin_list[1], n, m, count + 1, board, answer, dp
                )


n, m = list(map(int, get_input().strip().split()))

board = []
first_coin: tuple = None
second_coin: tuple = None
for i in range(n):
    b = get_input().strip()
    ls = []
    for j in range(len(b)):
        ls.append(b[j])
        if b[j] == "o":
            if first_coin is None:
                first_coin = (i, j)
            else:
                second_coin = (i, j)
    board.append(ls)

answer = []
dp = dict()
dp[(first_coin, second_coin)] = 0
move_coin(first_coin, second_coin, n, m, 0, board, answer, dp)

if answer:
    print(min(answer))
else:
    print(-1)
