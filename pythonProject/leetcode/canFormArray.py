from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        res = []

        for num in arr:
            res += mp.get(num, [])

        return res == arr


print(Solution().canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
