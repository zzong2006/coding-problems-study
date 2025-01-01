from sys import stdin, stdout
from sys import maxsize

m, n = map(int, stdin.readline().split())
a = [None] * m
queue = []
notZero = []
answer = 0

# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳
for i in range(m):
    a[i] = [int(x) for x in stdin.readline().split()]
    for j in range(n):
        if a[i][j] == 2:
            queue.append((i, j))
        if a[i][j] == 0:
            notZero.append((i, j))

b = [r[:] for r in a]
look = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다
for i in range(len(notZero)):
    for j in range(i + 1, len(notZero)):
        for k in range(j + 1, len(notZero)):
            for y, x in [notZero[i], notZero[j], notZero[k]]:
                a[y][x] = 1

            fakeQueue = queue.copy()
            # 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있음
            while len(fakeQueue) != 0:
                (y, x) = fakeQueue.pop()
                for z in range(len(look)):
                    addY, addX = look[z]
                    if (
                        m > y + addY >= 0
                        and n > x + addX >= 0
                        and a[y + addY][x + addX] == 0
                    ):
                        a[y + addY][x + addX] = 2
                        fakeQueue.append((y + addY, x + addX))

            # 얻을 수 있는 안전 영역 크기의 최댓값
            count = 0
            for ii in range(m):
                for jj in range(n):
                    if a[ii][jj] == 0:
                        count += 1
            answer = max(count, answer)
            a = [r[:] for r in b]

print(answer)
