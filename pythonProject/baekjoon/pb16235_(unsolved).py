# 나무 제테크

import sys

get_input = sys.stdin.readline

n, m, k = list(map(int, get_input().split()))

# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
# M개의 나무를 구매해 땅에 심었다. 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.

board = []
for i in range(n):
    board.append(list(map(int, get_input().split())))

# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.

