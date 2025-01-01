import sys
from collections import deque
import heapq

import bisect


def solution(n):
    # get_input = sys.stdin.readline
    # n = int(get_input().strip())
    # k = int(get_input().strip())

    arr = [2, 2, 5, 5, 5, 8, 10, 15]
    arr.sort()
    looking_for = n
    start = 0
    end = len(arr)

    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= looking_for:  # 같아도 오른쪽
            start = mid + 1
        else:
            end = mid
    answer = start
    assert bisect.bisect_right(arr, n) == answer

    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < looking_for:  # 같지 않음면 가만히 있음
            start = mid + 1
        else:
            end = mid
    answer = start
    assert bisect.bisect_left(arr, n) == answer
    return answer


for i in range(16):
    print(i, solution(i))
