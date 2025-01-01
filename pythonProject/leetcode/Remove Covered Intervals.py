from typing import List
from functools import cmp_to_key


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def is_cover(a: list, b: list):
            if b[0] <= a[0] and a[1] <= b[1]:
                return True
            else:
                return False

        def comp(a, b):
            if a[0] != b[0]:
                return -b[0] + a[0]
            else:
                return -a[1] + b[1]

        intervals.sort(key=cmp_to_key(comp))
        print(intervals)
        removed = set()
        for i in range(len(intervals)):
            if i not in removed:
                s, e = intervals[i]
                for j in range(i + 1, len(intervals)):
                    go, stop = intervals[j]
                    if e < go:
                        break
                    else:
                        if is_cover(intervals[j], intervals[i]):
                            removed.add(j)
        return len(intervals) - len(removed)


a = Solution()
print(a.removeCoveredIntervals([[1, 2], [1, 4], [3, 4]]))
