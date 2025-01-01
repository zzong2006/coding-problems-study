from collections import deque
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        end = 0
        start = 0
        total = None
        while end < n:
            if total is None:
                total = nums[end]
            else:
                total *= nums[end]
            if total < k:
                cnt += 1 + end - start
            else:
                while start < end:
                    div = nums[start]
                    total /= div
                    start += 1
                    if total < k:
                        cnt += 1 + end - start
                        break
            end += 1
        return cnt


a = Solution()
print(a.numSubarrayProductLessThanK([1, 2, 3], 0))
# print(a.numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19))
