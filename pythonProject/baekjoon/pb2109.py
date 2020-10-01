import sys
from collections import deque, defaultdict
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    if n == 0:
        return 0
    else:
        univ = []
        ls = []
        for i in range(n):
            univ.append(list(map(int, get_input().strip().split())))
        univ.sort(key=lambda x: (x[1], x[0]), reverse=True)
        max_day = univ[0][1]
        curr = 0
        total = 0
        for i in reversed(range(1, max_day + 1)):
            while curr < len(univ) and univ[curr][1] >= i:
                heapq.heappush(ls, -univ[curr][0])
                curr += 1
            if ls:
                t = heapq.heappop(ls)
                total += -t

        return total


print(solution())
