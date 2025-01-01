import sys
from collections import deque
from itertools import permutations


def solution():
    get_input = sys.stdin.readline
    a = int(get_input().strip())
    ops = get_input().strip()
    que = deque()

    if ops[0] == "-":
        for i in range(-10, 0, 1):
            que.append([i])
    elif ops[0] == "0":
        que.append([0])
    else:
        for i in range(1, 11):
            que.append([i])

    if a > 1:
        while que:
            a = que.pop()
            start = 0
            n = a
            for i in range(len(a)):
                start += n
                n -= 1
            # 숫자 고르고 체크
            pick = None
            if ops[start] == "-":
                for i in range(-10, 0, 1):
                    pick = i
            elif ops[start] == "0":
                pick = 0
            else:
                for i in range(1, 11):
                    pick = i
    else:
        return que.popleft()


res = solution()
for j in range(len(res)):
    print(j, end=" ")
