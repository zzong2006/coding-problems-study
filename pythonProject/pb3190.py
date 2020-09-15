class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = 0
        self.lists = [(self.x, self.y)]

    def move(self, move, N, board):
        # 머리를 꺼냄
        (x, y) = self.lists[-1]
        addX, addY = move[self.direction]
        if 1 <= x + addX <= N and 1 <= y + addY <= N:
            if board[y + addY][x + addX] == 2:
                return False
            elif board[y + addY][x + addX] == 1:  # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
                self.lists.append((x + addX, y + addY))
                (a, b) = self.lists[-1]
                board[b][a] = 2
                return True
            else:  # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
                (a, b) = self.lists[0]
                board[b][a] = 0
                for i in range(1, len(self.lists)):
                    self.lists[i - 1] = self.lists[i]
                x += addX
                y += addY
                board[y][x] = 2
                self.lists[-1] = (x, y)
                return True
        else:
            return False

    def change(self, to: str):
        if to == "D":
            self.direction += 1
            self.direction %= 4
        else:
            self.direction -= 1
            if self.direction < 0:
                self.direction += 4


N = int(input())
K = int(input())
apples = [tuple(map(int, input().split())) for _ in range(K)]
L = int(input())
order = []
for i in range(L):
    a = list(input().split())
    order.append((int(a[0]), a[1]))
order = order[::-1]


tick = 0
direction = 0
# 0 : 오른쪽 , 1: 남쪽, 2: 서쪽, 3 : 북쪽
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

sk = Snake(1, 1)

# 0: 빈 공간, 1: 사과, 2: 뱀
board = [[0] * (N + 1) for _ in range(N + 1)]
for (y, x) in apples:
    board[y][x] = 1
board[1][1] = 2

game_over = False
while not game_over:
    tick += 1
    if not sk.move(move, N, board):
        break
    else:
        if len(order) > 0 and tick == order[-1][0]:
            sk.change(order[-1][1])
            order.pop()
print(tick)
