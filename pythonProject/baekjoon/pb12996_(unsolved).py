from collections import deque
import sys


def solution():
    def dfs(a, b, c, curr_set, target):
        if len(curr_set) == target and a <= 0 and b <= 0 and c <= 0:
            p_set.add(tuple(sorted(curr_set)))
        elif len(curr_set) < target:
            copied_set = curr_set.copy()
            copied_set.append('A')
            dfs(a - 1, b, c, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('B')
            dfs(a, b - 1, c, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('C')
            dfs(a, b, c - 1, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('AB')
            dfs(a - 1, b - 1, c, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('BC')
            dfs(a, b - 1, c - 1, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('AC')
            dfs(a - 1, b, c - 1, copied_set, target)
            copied_set = curr_set.copy()
            copied_set.append('ABC')
            dfs(a - 1, b - 1, c - 1, copied_set, target)

    p_set = set()
    dfs(1, 1, 1, list(), 3)

    print(p_set)
    print(len(p_set))
solution()

# 3 1 1 1
# 6

# 50 10 10 10
# 0
