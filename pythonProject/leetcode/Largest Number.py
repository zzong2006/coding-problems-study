from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a = sorted(
            nums,
            key=cmp_to_key(lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))),
        )
        output = ""
        all_zero = True
        for i in a:
            output += str(i)
            if all_zero and i != 0:
                all_zero = False
        if all_zero:
            output = "0"
        return output


a = Solution()

print(a.largestNumber([0, 0]))
