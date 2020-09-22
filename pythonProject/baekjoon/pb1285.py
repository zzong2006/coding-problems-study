"""
greedy : 행 열 중에 가장 많은 H (0)를 가진 행 또는 열을 뒤집는다.
"""

import sys
from itertools import combinations

get_input = sys.stdin.readline

n = int(get_input().strip())

board = []
for i in range(n):
    a = get_input().strip()
    b = []
    for j in a:
        if j == 'H':
            b.append(0)
        else:
            b.append(1)
    board.append(b)

a = set()
a.add(tuple(map(tuple, board)))

print(a)
