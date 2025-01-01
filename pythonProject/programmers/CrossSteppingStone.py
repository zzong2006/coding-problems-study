import heapq
from collections import deque


def solution(stones, k):
    a = min(stones)
    b = max(stones)

    results = []
    dq = deque()

    for i in range(k):
        while dq and stones[i] >= stones[dq[-1]]:
            dq.pop()
        dq.append(i)

    for i in range(k, len(stones)):
        results.append(stones[dq[0]])
        # out of index
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and stones[dq[-1]] <= stones[i]:
            dq.pop()
        dq.append(i)

    results.append(stones[dq[0]])
    # print(results)
    answer = min(results)
    return answer


print(solution([10, 4, 0, 0, 99, 0, 20, 11, 0, 0, 11], 4))
