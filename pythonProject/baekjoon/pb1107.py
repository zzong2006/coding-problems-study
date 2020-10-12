import sys
from collections import deque, defaultdict
from itertools import permutations


def solution():
    def backtrack(vv, ans):
        st = ans
        if len(n) - 1 <= len(vv) <= len(n) + 1:
            st = min(st, len(vv) + abs(int(vv) - int(n)))

        if len(vv) < len(n) + 1 and len(vv) < 6:
            for ke in a.keys():
                st = min(st, backtrack(vv + str(ke), st))
        return st
    get_input = sys.stdin.readline
    n = get_input().strip()
    m = int(get_input().strip())
    a = defaultdict(bool)
    if m > 0:
        board = list(map(int, get_input().strip().split()))
    else:
        board = []
    for i in range(10):
        if i not in board:
            a[i] = True
    answer = abs(int(n) - 100)
    if len(a.keys()) == 0:  # 모든 키 고장
        return answer

    que = deque()
    for k in a.keys():
        answer = min(answer, backtrack(str(k), answer))

    return answer


print(solution())
