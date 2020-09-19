from math import log, log10
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ls = "123456789"
        a = int(log10(low)) + 1
        b = int(log10(high)) + 1
        output = []
        for a in range(a, b + 1):
            for i in range(len(ls) - a + 1):
                z = int(ls[i:i + a])
                if low <= z <= high:
                    output.append(z)
        return output


a = Solution()
print(a.sequentialDigits(low=1000, high=13000))