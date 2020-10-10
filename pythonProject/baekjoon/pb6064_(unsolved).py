from collections import deque
import sys


def solution():
    get_input = sys.stdin.readline

    m = list(map(int, get_input().split()))[0]

    for i in range(m):
        m, n, x_target, y_target = list(map(int, get_input().split()))
        count = 1
        x, y = 1, 1
        visited = False
        while x_target != x or y_target != y:
            if x_target == x and y < y_target:
                visited = True
                if x < m:
                    x += 1
                else:
                    x = 1
                if y < n:
                    y += 1
                else:
                    y = 1
                count += 1
            print(x, y, x-y, abs(y-x), count)
        else:
            print(count)


solution()
