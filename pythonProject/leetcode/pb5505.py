# 5505. Maximum Sum Obtained of Any Permutation
from typing import List
from itertools import permutations


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        maximum = 0
        vals = [0] * len(nums)
        for start, end in requests:
            vals[1:3] += 1
            for x in range(start, end + 1):
                vals[x] += 1
        nums.sort(reverse=True)
        vals.sort(reverse=True)
        total = 0
        for a, b in zip(nums, vals):
            total += (a * b)
            total %= (10 ** 9 + 7)

        return total


a = Solution()
print(a.maxSumRangeQuery([1, 2, 3, 4, 5], [[1, 3], [0, 1]]))
print(a.maxSumRangeQuery([1, 2, 3, 4, 5], [[1, 3], [0, 1]]))
print(a.maxSumRangeQuery([1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]]))
