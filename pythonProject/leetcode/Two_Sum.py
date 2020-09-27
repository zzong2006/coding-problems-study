from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(0, len(nums)):
            sub = target - nums[i]
            if sub in d and d[sub] != i:
                return [i, d[sub]]


a = Solution()
a.twoSum([2, 3, 7], 10)
