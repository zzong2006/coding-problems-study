import heapq

def solution(n, times):
    answer = 0
    ls = []
    for idx, t in enumerate(times):
        heapq.heappush(ls, [0, t])

    for i in range(n):
        # curr, t = heapq.heappop(ls)
        heapq.heapreplace(ls, [ls[0][0] + ls[0][1], ls[0][1]])
        print(ls)
    print(ls)
    return answer

print(solution(6, [7, 10]))