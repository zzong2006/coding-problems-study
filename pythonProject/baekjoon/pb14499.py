"""
  2
4 1 3
  5
  6
주사위 전개도
"""


def swap(d, str1, str2):
    temp = d[str1]
    s[str1] = d[str2]
    d[str2] = temp


# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
def roll(d: dict, direction: int):
    new_d = d.copy()
    if direction == 1:  # not change north and south
        new_d["west"] = d["up"]
        new_d["east"] = d["down"]
        new_d["up"] = d["east"]
        new_d["down"] = d["west"]
    if direction == 2:
        new_d["west"] = d["down"]
        new_d["east"] = d["up"]
        new_d["up"] = d["west"]
        new_d["down"] = d["east"]
    if direction == 3:  # not change west and east
        new_d["south"] = d["up"]
        new_d["north"] = d["down"]
        new_d["up"] = d["north"]
        new_d["down"] = d["south"]
    if direction == 4:  # not change west and east
        new_d["south"] = d["down"]
        new_d["north"] = d["up"]
        new_d["up"] = d["south"]
        new_d["down"] = d["north"]
    return new_d


dice = {"up": 0, "down": 0, "north": 0, "west": 0, "east": 0, "south": 0}

n, m, y, x, k = list(map(int, input().split()))

board = [[int(x) for x in input().split()] for _ in range(n)]
order = list(map(int, input().split()))
answer = []
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for od in order:
    #  동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    # move
    moveX, moveY = move[od - 1]
    if 0 <= x + moveX < m and 0 <= y + moveY < n:
        x += moveX
        y += moveY
        dice = roll(dice, od)
        if (
            board[y][x] == 0
        ):  # 이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
            board[y][x] = dice["down"]
        else:  # 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다
            dice["down"] = board[y][x]
            board[y][x] = 0
        answer.append(dice["up"])

for i in range(len(answer)):
    print(answer[i])
