import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    a, b, c = list(map(int, get_input().strip().split()))

    que = deque()
    que.append((a, b, c))
    visited = set()

    while que:
        z, x, y = que.popleft()
        # print(z, x, y)
        if z == x == y:
            return 1
        if (z, x, y) not in visited:
            visited.add((z, x, y))
            # z > x
            if z > x and z - x > 0:
                que.append((z - x, x + x, y))
            elif z <= x and x - z > 0:
                que.append((z + z, x - z, y))
            if x > y and x - y > 0:
                que.append((z, x - y, y + y))
            elif x <= y and y - x > 0:
                que.append((z, x + x, y - x))
            if z > y and z - y > 0:
                que.append((z - y, x, y + y))
            elif z <= y and y - z > 0:
                que.append((z + z, x, y - z))

    return 0


print(solution())
