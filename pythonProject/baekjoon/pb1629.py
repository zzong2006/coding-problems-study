import math
import sys


def solution():
    def search(curr):
        if curr in memo:
            return memo[curr]
        else:
            if curr % 2 == 0:
                memo[curr] = (search(curr // 2) ** 2) % c
            else:
                memo[curr] = (search(curr // 2) ** 2 * a) % c
        return memo[curr]

    get_input = sys.stdin.readline

    a, b, c = list(map(int, get_input().strip().split()))
    memo = dict()
    memo[1] = a % c
    memo[0] = 1 % c
    search(b)
    return memo[b]


print(solution())
