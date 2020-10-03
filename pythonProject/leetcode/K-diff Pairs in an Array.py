from collections import Counter
from typing import List
from itertools import combinations


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        output = 0
        if k == 0:
            count_nums = Counter(nums)
            for i in count_nums.keys():
                if count_nums[i] > 1:
                    output += 1
        else:
            set_nums = set(nums)
            sorted_nums = sorted(list(set_nums))
            for w in range(len(sorted_nums) - 1):
                ma = sorted_nums[w]
                for q in range(w + 1, len(sorted_nums)):
                    res = sorted_nums[q] - ma
                    if res == k:
                        output += 1
                        break
                    elif res > k:
                        break
        return output


a = Solution()
# print(a.findPairs([1, 2, 4, 4, 3, 3, 0, 9, 2, 3], 3))
print(a.findPairs([3, 1, 4, 1, 5], 2))
print(a.findPairs([-1, -2, -3], 1))
