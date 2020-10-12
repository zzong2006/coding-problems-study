import sys
from collections import deque, defaultdict
from itertools import permutations
import heapq


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    ls = [[0, n]]
    heapq.heapify(ls)
    dp = [sys.maxsize] * 100001
    dd = defaultdict(int)
    dd[n] = -1
    dp[n] = 0
    while ls:
        t, p = heapq.heappop(ls)

        if p == k:
            break
        else:
            if 0 <= p - 1 and dp[p - 1] > t + 1:
                heapq.heappush(ls, [t + 1, p - 1])
                dd[p - 1] = p
                dp[p - 1] = t + 1
            if p + 1 < len(dp) and dp[p + 1] > t + 1:
                heapq.heappush(ls, [t + 1, p + 1])
                dd[p + 1] = p
                dp[p + 1] = t + 1
            if p * 2 < len(dp) and dp[p * 2] > t + 1:
                heapq.heappush(ls, [t + 1, p * 2])
                dd[p * 2] = p
                dp[p * 2] = t + 1
    print(t)
    st = k
    ans = [k]
    # print(dd)
    while dd[st] != -1:
        ans.append(dd[st])
        st = dd[st]
    print(' '.join(list(map(str, ans[::-1]))))

    # print(routes)


solution()
