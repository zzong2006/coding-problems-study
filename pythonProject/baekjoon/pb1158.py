from collections import deque
import sys


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    que = deque()
    for i in range(n):
        que.append(i + 1)
    visited = set()
    ls = []
    curr = 0
    while que:
        # step = k % (len(que) + 1)
        for ii in range(k - 1):
            a = que.popleft()
            que.append(a)
        a = que.popleft()
        ls.append(a)
        # print(que)
    print("<", end="")
    for i in range(n):
        if i != n - 1:
            print("{}, ".format(ls[i]), end="")
        else:
            print("{}>".format(ls[i]), end="")


solution()
