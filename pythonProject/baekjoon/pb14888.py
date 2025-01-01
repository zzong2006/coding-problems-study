import sys
import heapq
from collections import deque
from math import inf


def solution():
    get_input = sys.stdin.readline
    n = list(map(int, get_input().strip().split()))[0]
    board = list(map(int, get_input().strip().split()))
    ops = list(map(int, get_input().strip().split()))

    que = deque()
    que.append([board[0], ops.copy(), 0])
    max_val = -float(inf)
    min_val = float(inf)

    while que:
        curr, curr_ops, idx = que.popleft()
        # print(curr, curr_ops, idx)
        if idx == n - 1:
            max_val = max(max_val, curr)
            min_val = min(min_val, curr)
        else:
            for i in range(4):
                if curr_ops[i] > 0:
                    copied_ops = curr_ops.copy()
                    copied_ops[i] -= 1
                    # +, -, x, /
                    if i == 0:
                        que.append([curr + board[idx + 1], copied_ops, idx + 1])
                    elif i == 1:
                        que.append([curr - board[idx + 1], copied_ops, idx + 1])
                    elif i == 2:
                        que.append([curr * board[idx + 1], copied_ops, idx + 1])
                    elif i == 3:
                        temp_num = abs(curr) // board[idx + 1]
                        if curr < 0:
                            temp_num *= -1
                        que.append([temp_num, copied_ops, idx + 1])
    print(max_val)
    print(min_val)


solution()
