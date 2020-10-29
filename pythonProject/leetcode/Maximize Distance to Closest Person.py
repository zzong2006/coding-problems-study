import itertools
from typing import List
import sys


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * n
        right = [0] * n
        if seats[0] == 0:
            left[0] = sys.maxsize
        if seats[n - 1] == 0:
            right[n - 1] = sys.maxsize

        for i in range(1, n):
            if seats[i]:
                left[i] = 0
            else:
                left[i] = left[i - 1] + 1
        for j in reversed(range(n - 1)):
            if seats[j]:
                right[j] = 0
            else:
                right[j] = right[j + 1] + 1
        print(left, right)
        answer = 0
        for i in range(n):
            answer = max(answer, min(left[i], right[i]))
        return answer

    def max_dist_to_closest_2(self, seats: List[int]) -> int:
        # generator 생성
        people = (i for i, seat in enumerate(seats) if seat)
        # print(list(people))
        prev, future = None, next(people)
        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))
                print(left, right, ans)
        return ans


a = Solution()
print(a.max_dist_to_closest_2([1, 0, 0, 0, 1, 0, 1]))
print(a.maxDistToClosest([1, 0, 0, 0]))
print(a.maxDistToClosest([0, 1]))
