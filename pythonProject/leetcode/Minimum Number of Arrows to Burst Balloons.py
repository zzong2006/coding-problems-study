from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if points:
            points.sort(key=lambda x: (x[0], x[1]))
            start, end = points[0]
            count = 1
            for i in range(1, len(points)):
                a, b = points[i]
                if end < a or b < start :
                    count += 1
                    start = a
                    end = b
                else:
                    start = max(start, a)
                    end = min(end, b)
        else:
            count = 0
        return count

a = Solution()
print(a.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
