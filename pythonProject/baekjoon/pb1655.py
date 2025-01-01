import sys
from collections import Counter

import heapq


def solution():
    get_input = sys.stdin.readline

    n = int(get_input().strip())
    min_heap = []
    max_heap = []
    for i in range(n):
        k = int(get_input().strip())
        if not max_heap:
            max_heap.append(-k)
        elif not min_heap:
            min_heap.append(k)
        else:
            if len(max_heap) == len(min_heap):
                heapq.heappush(max_heap, -k)
            elif len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, k)

        if max_heap and min_heap and -max_heap[0] > min_heap[0]:
            xh = heapq.heappop(max_heap)
            nh = heapq.heappop(min_heap)
            heapq.heappush(min_heap, -xh)
            heapq.heappush(max_heap, -nh)
        # print(min_heap, max_heap)
        print(-max_heap[0])


solution()
