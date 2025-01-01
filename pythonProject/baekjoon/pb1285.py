"""
greedy : 행 열 중에 가장 많은 H (0)를 가진 행 또는 열을 뒤집는다.
"""

import sys
from typing import List
from itertools import combinations

get_input = sys.stdin.readline

n = int(get_input().strip())

board = [[0] * n for _ in range(n)]
for w in range(n):
    a = get_input().strip()
    for j in range(n):
        if a[j] == "H":
            board[w][j] = 0
        else:
            board[w][j] = 1

answer = sys.maxsize


for w in range(0, 1 << n):
    visited = [False] * (n + 1)
    for i in range(n):
        if (1 << i) & w:
            visited[i] = True

    count = 0

    for i in range(n):
        one_count = 0
        for k in range(n):
            if board[k][i] == 1 and visited[k] is False:
                one_count += 1
            elif board[k][i] == 0 and visited[k] is True:
                one_count += 1
        if one_count > n - one_count:
            count += n - one_count  # 뒤집
        else:
            count += one_count

    answer = min(answer, count)
print(answer)
# 가장 첫번째 가로 행 뒤집
