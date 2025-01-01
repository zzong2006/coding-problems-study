import heapq


def solution(n, times):
    def get_count(t):
        count = 0
        for i in range(len(times)):
            count += t // times[i]
        return count

    b = n * max(times)
    a = 0
    while a < b:
        mid = (a + b) // 2
        k = get_count(mid)
        if k < n:
            a = mid + 1
        else:
            b = mid
            answer = mid

    return answer


print(solution(6, [7, 10]))
