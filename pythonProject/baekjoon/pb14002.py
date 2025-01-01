import sys
import heapq
import bisect
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = list(map(int, get_input().split()))

    ls = [list() for i in range(n)]
    ls[0] = [board[0]]
    for i in range(1, n):
        for j in range(i):
            if ls[j][-1] < board[i] and len(ls[i]) < len(ls[j]) + 1:
                ls[i] = ls[j] + [board[i]]
        if not ls[i]:
            ls[i] = [board[i]]

    answer = max(ls, key=lambda x: len(x))
    print(len(answer))

    for i in range(len(answer)):
        print(answer[i], end=" ")

    # return len(ls)


solution()
