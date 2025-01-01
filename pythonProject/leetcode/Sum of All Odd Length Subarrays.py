# 5503. Sum of All Odd Length Subarrays

from itertools import combinations
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        al = len(arr)
        summation = 0
        for i in range(1, len(arr) + 1):
            if i % 2 != 0:
                for x in range(len(arr) - i + 1):
                    summation += sum(arr[x : x + i])

        return summation


a = Solution()
print(a.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
print(a.sumOddLengthSubarrays([1, 2]))
print(a.sumOddLengthSubarrays([10, 11, 12]))
