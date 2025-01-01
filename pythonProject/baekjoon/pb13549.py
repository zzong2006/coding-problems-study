import sys
from collections import deque
import heapq

get_input = sys.stdin.readline

n, k = list(map(int, get_input().split()))

dp = [sys.maxsize] * 200002

que = []
heapq.heapify(que)
heapq.heappush(que, [0, n])

while len(que) > 0:
    sec, curr = heapq.heappop(que)

    if curr != k:
        for x in [-1, 1]:
            new_curr = curr + x
            if 0 <= new_curr < 200002 and dp[new_curr] > sec + 1:
                dp[new_curr] = sec + 1
                heapq.heappush(que, [(sec + 1), new_curr])

        new_curr = curr * 2
        if 0 <= new_curr < 200002 and dp[new_curr] > sec:
            dp[new_curr] = sec
            heapq.heappush(que, [sec, new_curr])
    else:
        break
if k == n:
    print(0)
else:
    print(dp[k])
