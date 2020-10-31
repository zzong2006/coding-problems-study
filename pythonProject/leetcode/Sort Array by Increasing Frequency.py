from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        # print(cnt)
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums


a = Solution()
print(a.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
