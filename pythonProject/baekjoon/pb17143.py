import sys
from collections import deque, defaultdict
from itertools import combinations
import heapq


def solution():
    get_input = sys.stdin.readline
    r, c, m = list(map(int, get_input().strip().split()))
    sharks = set()

    for i in range(m):
        sharks.add(tuple(map(int, get_input().strip().split())))

    pos = 0
    answer = 0
    if m != 0:
        while pos < c:
            # 이동
            pos += 1
            # 상어 삭제
            most_closed = None
            for shark in sharks:
                y, x, s, d, z = shark
                if x == pos:
                    if most_closed is None:
                        most_closed = shark
                    else:
                        if most_closed[0] > shark[0]:
                            most_closed = shark

            if most_closed is not None:
                answer += most_closed[4]
                sharks.remove(most_closed)
            new_sharks = dict()
            # 상어 움직임 (핵심)
            while sharks:
                shark = sharks.pop()
                # print('from ', shark)
                y, x, s, d, z = shark
                # s 가 1000일 가능성이 있음 있음 !
                if d == 1:  # 위
                    if y - s <= 0:
                        sub_s = s - (y - 1)
                        what = sub_s // (r - 1)
                        rem = sub_s % (r - 1)
                        if what % 2 != 0:
                            y = r - rem
                            if rem == 0:
                                d = 2
                            else:
                                d = 1
                        else:
                            y = 1 + rem
                            if rem == 0:
                                d = 1
                            else:
                                d = 2
                    else:
                        y -= s
                elif d == 2:  # 아래
                    if y + s > r:
                        sub_s = s - (r - y)
                        what = sub_s // (r - 1)
                        rem = sub_s % (r - 1)
                        if what % 2 == 0:
                            y = r - rem
                            if rem == 0:
                                d = 2
                            else:
                                d = 1
                        else:
                            y = 1 + rem
                            if rem == 0:
                                d = 1
                            else:
                                d = 2
                    else:
                        y += s
                elif d == 3:  # 오른쪽
                    if x + s > c:
                        sub_s = s - (c - x)
                        what = sub_s // (c - 1)
                        rem = sub_s % (c - 1)
                        if what % 2 == 0:
                            x = c - rem
                            if rem == 0:
                                d = 3
                            else:
                                d = 4
                        else:
                            x = 1 + rem
                            if rem == 0:
                                d = 4
                            else:
                                d = 3
                    else:
                        x += s
                elif d == 4:  # 왼쪽
                    if x - s <= 0:
                        sub_s = s - (x - 1)
                        what = sub_s // (c - 1)
                        rem = sub_s % (c - 1)
                        if what % 2 == 0:
                            x = 1 + rem
                            if rem == 0:
                                d = 4
                            else:
                                d = 3
                        else:
                            x = c - rem
                            if rem == 0:
                                d = 3
                            else:
                                d = 4
                    else:
                        x -= s
                # print('from ', [y, x, s, d, z])
                if (y, x) not in new_sharks:
                    new_sharks[(y, x)] = (y, x, s, d, z)
                else:
                    if new_sharks[(y, x)][4] < z:
                        new_sharks[(y, x)] = (y, x, s, d, z)

            sharks.clear()
            # 겹친 상어 정리 (크기가 서로 같다면? 두 상어가 같은 크기를 갖는 경우는 없다)
            for shark in new_sharks.values():
                sharks.add(shark)

    return answer


print(solution())
