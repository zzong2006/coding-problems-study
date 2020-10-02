import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    assign = []
    for i in range(n):
        assign.append(list(map(int, get_input().strip().split())))

    assign.sort(key=lambda x:(x[0], x[1]), reverse=True)
    max_day = assign[0][0]
    ls = []
    hap = 0
    j = 0
    # print(assign)
    for i in reversed(range(1, max_day + 1)):
        while j < len(assign):
            if assign[j][0] >= i:
                heapq.heappush(ls, -assign[j][1])
                j += 1
            else:
                break
        if ls:
            # print(ls)
            hap += -heapq.heappop(ls)
    return hap

print(solution())