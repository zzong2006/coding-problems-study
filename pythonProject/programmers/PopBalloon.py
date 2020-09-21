# 못풀었음

from math import log

def solution(a):
    answer = 0
    remains = sorted(a)
    N = len(a)
    bigger = dict()
    for i in range(N):
        bigger[remains[i]] = N - i - 1

    left = 0
    right = N - 1
    dp = bigger[a[0]]

    for i in range(N):
        new_left = left

    return answer


print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
