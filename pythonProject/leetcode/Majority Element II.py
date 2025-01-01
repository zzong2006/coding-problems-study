"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        th = n // 3
        first = None
        count_first = 0
        second = None
        count_second = 0
        for i in range(n):
            if first is None:
                first = nums[i]
                count_first = 1
                continue
            elif second is None and first != nums[i]:
                second = nums[i]
                count_second = 1
            else:
                if first == nums[i]:
                    count_first += 1
                elif second == nums[i]:
                    count_second += 1
                else:
                    if count_first == 0:
                        first = nums[i]
                        count_first = 1
                    elif count_second == 0:
                        second = nums[i]
                        count_second = 1
                    elif count_first != 0 and count_second != 0:
                        count_first -= 1
                        count_second -= 1
        answer = []
        if nums.count(first) > th:
            answer.append(first)
        if second not in answer and nums.count(second) > th:
            answer.append(second)

        return answer


a = Solution()
print(a.majorityElement([3, 2, 3]))
