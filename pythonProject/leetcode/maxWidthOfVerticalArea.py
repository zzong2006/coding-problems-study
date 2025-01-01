from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        answer = 0
        start = points[0][0]
        for i in range(1, len(points)):
            answer = max(answer, points[i][0] - start)
            start = points[i][0]

        return answer


a = Solution()
print(a.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
print(a.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))
