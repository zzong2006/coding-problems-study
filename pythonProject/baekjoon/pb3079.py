import sys


def solution():
    def total_num(t):
        total = 0
        for j in range(len(ls)):
            total += (t // ls[j])
        return total

    n, m = list(map(int, sys.stdin.readline().split()))
    ls = []
    start = 0
    end = 0
    for i in range(n):
        ls.append(int(sys.stdin.readline()))
        end = max(ls[-1] * m, end)

    answer = end
    while start < end:
        mid = (start + end) // 2
        count = total_num(mid)
        if count >= m:
            end = mid
            answer = min(answer, mid)
        elif count < m:
            start = mid + 1
    return answer


print(solution())
