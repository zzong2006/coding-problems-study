import sys
from itertools import combinations

get_input = sys.stdin.readline

n, m = list(map(int, get_input().split()))

board = []
for i in range(n):
    board.append(list(map(int, get_input().split())))

chicken_list = []
curr = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            chicken_list.append((curr, i, j))

man_list = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            dist = []
            for _, y, x in chicken_list:
                dist.append(abs(y - i) + abs(x - j))
            man_list.append(dist)

min_sum = sys.maxsize
for z in range(1, m + 1):
    for comb in combinations(range(len(chicken_list)), z):
        curr = 0
        for i in range(len(man_list)):
            min_val = 0
            for k in range(len(comb)):
                if k == 0:
                    min_val = man_list[i][comb[k]]
                else:
                    min_val = min(min_val, man_list[i][comb[k]])
            curr += min_val
        min_sum = min(min_sum, curr)

print(min_sum)