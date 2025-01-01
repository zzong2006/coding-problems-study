from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ls = []
        heapq.heapify(ls)

        for i in stones:
            heapq.heappush(ls, -i)

        while len(ls) > 1:
            a = heapq.heappop(ls)
            b = heapq.heappop(ls)

            if -a > -b:
                heapq.heappush(ls, a - b)
        if ls:
            return -ls[-1]
        else:
            return 0
