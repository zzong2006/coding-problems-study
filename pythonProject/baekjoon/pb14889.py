import sys
from collections import deque
from itertools import combinations


def solution():
    def get_score(cb):
        output = 0
        for x, y in combinations(cb, 2):
            output += board[x][y] + board[y][x]
        return output

    answer = sys.maxsize
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    board = []
    for i in range(n):
        board.append(list(map(int, get_input().strip().split())))
    visited_comb = set()
    for comb in combinations(range(n), n // 2):
        print(comb)
        if comb not in visited_comb:
            other_comb = tuple([x for x in range(n) if x not in comb])
            visited_comb.add(comb)
            visited_comb.add(other_comb)
            a = get_score(comb)
            b = get_score(other_comb)
            answer = min(abs(a - b), answer)

    print(answer)


solution()
