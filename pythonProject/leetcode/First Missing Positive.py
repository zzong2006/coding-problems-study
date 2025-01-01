from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        else:
            max_val = max(nums)
            if max_val <= 0:
                return 1
            else:
                num_set = set(nums)
                for i in range(1, max_val):
                    if i not in num_set:
                        return i
                return max_val + 1


a = Solution()
print(a.firstMissingPositive([3, 4, -1, 1]))
