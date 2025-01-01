import sys
from collections import deque
from itertools import combinations


def solution():
    def check(bd: list):
        for aa in range(n):
            for bb in range(n):
                if bd[aa][bb] == 0:
                    return False
        return True

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    board = [[0] * n for _ in range(n)]
    virus = []
    num_virus = 0
    for i in range(n):
        ls = list(map(int, get_input().strip().split()))
        for j in range(n):
            board[i][j] = ls[j]
            if ls[j] == 2:
                virus.append((i, j))
                num_virus += 1
    answer = sys.maxsize
    for comb in combinations(virus, num_virus - m):
        # comb 은 비활성화 바이러스
        copied_board = [board[i][:] for i in range(n)]
        for a, b in comb:
            copied_board[a][b] = 3
        real_virus = []
        # 바이러스 퍼트리기
        que = deque()
        for a, b in virus:
            if copied_board[a][b] == 2:
                que.append([(a, b), 0])
        max_time = 0
        while que:
            (y, x), t = que.popleft()

            for add_y, add_x in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                new_y = y + add_y
                new_x = x + add_x

                if (
                    0 <= new_y < n
                    and 0 <= new_x < n
                    and copied_board[new_y][new_x] == 0
                ):
                    copied_board[new_y][new_x] = 2
                    que.append([(new_y, new_x), t + 1])
            max_time = max(t, max_time)
        if check(copied_board):
            answer = min(max_time, answer)
    if answer == sys.maxsize:
        return -1
    else:
        return answer


print(solution())
