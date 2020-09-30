import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    jewels = []

    for i in range(n):
        jewels.append(list(map(int, get_input().strip().split())))
    bags = []
    for i in range(k):
        bags.append(int(get_input().strip()))
    jewels.sort(key=lambda x: (x[0], x[1]))
    bags.sort()
    curr = 0
    answer = 0
    ls = []
    for v in bags:
        while curr < len(jewels) and v >= jewels[curr][0]:
            heapq.heappush(ls, -jewels[curr][1])
            curr += 1
        if ls:
            answer += -(heapq.heappop(ls))

    return answer


print(solution())
