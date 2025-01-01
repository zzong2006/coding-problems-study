import heapq
import math
from collections import deque


def solution(board):
    def rotate_based_on_axis(ax, ro, clock):
        ax_y, ax_x = ax
        ro_y, ro_x = ro
        # 축 왼쪽에 회전이 존재
        if (ax_y == ro_y and ax_x - 1 == ro_x) or (ax_y == ro_y and ax_x + 1 == ro_x):
            # 위로 회전 (시계 방향)
            if clock:
                if (
                    0 <= ro_y - 1 < n
                    and 0 <= ax_y - 1 < n
                    and board[ro_y - 1][ro_x] == 0
                    and board[ax_y - 1][ax_x] == 0
                ):
                    return ax_y, ax_x, ax_y - 1, ax_x
            else:  # 반시계 방향
                if (
                    0 <= ro_y + 1 < n
                    and 0 <= ax_y + 1 < n
                    and board[ro_y + 1][ro_x] == 0
                    and board[ax_y + 1][ax_x] == 0
                ):
                    return ax_y, ax_x, ax_y + 1, ax_x
        # 오른쪽에 회전이 존재

        # 위쪽에 회전이 존재
        elif (ax_y == ro_y - 1 and ax_x == ro_x) or (ax_y == ro_y + 1 and ax_x == ro_x):
            if clock:
                if (
                    0 <= ax_x + 1 < n
                    and 0 <= ro_x + 1 < n
                    and board[ro_y][ro_x + 1] == 0
                    and board[ax_y][ax_x + 1] == 0
                ):
                    return ax_y, ax_x, ax_y, ax_x + 1
            else:  # 반시계 방향
                if (
                    0 <= ax_x - 1 < n
                    and 0 <= ro_x - 1 < n
                    and board[ro_y][ro_x - 1] == 0
                    and board[ax_y][ax_x - 1] == 0
                ):
                    return ax_y, ax_x, ax_y, ax_x - 1
        # 아래쪽에 회전이 존재

    # 아래쪽에 회전이 존재

    answer = 0
    pos = (0, 0, 0, 1)
    hashmap = dict()
    hashmap[pos] = 0
    hashmap[(0, 1, 0, 0)] = 0
    n = len(board)

    hq = []
    heapq.heappush(hq, (0, pos))
    while hq:
        count, curr = heapq.heappop(hq)
        a, b, c, d = curr
        if (a == n - 1 and b == n - 1) or (c == n - 1 and d == n - 1):
            return count
        # 회전
        for i in range(2):
            new_pos = rotate_based_on_axis((a, b), (c, d), i)
            if new_pos:
                other_new_pos = (new_pos[2], new_pos[3], new_pos[0], new_pos[1])
                if (
                    0 <= new_pos[0] < n
                    and 0 <= new_pos[2] < n
                    and 0 <= new_pos[1] < n
                    and 0 <= new_pos[3] < n
                    and ((new_pos not in hashmap) or (hashmap[new_pos] > count + 1))
                    and (
                        other_new_pos not in hashmap
                        or hashmap[other_new_pos] > count + 1
                    )
                    and board[new_pos[0]][new_pos[1]] == 0
                    and board[new_pos[2]][new_pos[3]] == 0
                ):
                    hashmap[new_pos] = count + 1
                    hashmap[other_new_pos] = count + 1
                    heapq.heappush(hq, (count + 1, new_pos))

            new_pos = rotate_based_on_axis((c, d), (a, b), i)
            if new_pos:
                other_new_pos = (new_pos[2], new_pos[3], new_pos[0], new_pos[1])
                if (
                    0 <= new_pos[0] < n
                    and 0 <= new_pos[2] < n
                    and 0 <= new_pos[1] < n
                    and 0 <= new_pos[3] < n
                    and ((new_pos not in hashmap) or (hashmap[new_pos] > count + 1))
                    and (
                        other_new_pos not in hashmap
                        or hashmap[other_new_pos] > count + 1
                    )
                    and board[new_pos[0]][new_pos[1]] == 0
                    and board[new_pos[2]][new_pos[3]] == 0
                ):
                    hashmap[new_pos] = count + 1
                    hashmap[other_new_pos] = count + 1
                    heapq.heappush(hq, (count + 1, new_pos))
        # 상/하/좌/우
        for y, x in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_pos = (a + y, b + x, c + y, d + x)
            other_new_pos = (c + y, d + x, a + y, b + x)

            if (
                0 <= new_pos[0] < n
                and 0 <= new_pos[2] < n
                and 0 <= new_pos[1] < n
                and 0 <= new_pos[3] < n
                and ((new_pos not in hashmap) or (hashmap[new_pos] > count + 1))
                and (other_new_pos not in hashmap or hashmap[other_new_pos] > count + 1)
                and board[new_pos[0]][new_pos[1]] == 0
                and board[new_pos[2]][new_pos[3]] == 0
            ):
                hashmap[new_pos] = count + 1
                hashmap[other_new_pos] = count + 1
                heapq.heappush(hq, (count + 1, new_pos))

    return answer


print(
    solution(
        [
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0],
        ]
    )
)
