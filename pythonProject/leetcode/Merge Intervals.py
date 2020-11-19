from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        answer = []
        prev_x = None
        prev_y = None
        for x, y in intervals:
            if prev_x is None:
                prev_x = x
                prev_y = y
            else:
                if (prev_y < x) or (y < prev_x):
                    answer.append([prev_x, prev_y])
                    prev_x = x
                    prev_y = y
                else:
                    prev_x = min(prev_x, x)
                    prev_y = max(prev_y, y)
            print(prev_x, prev_y)
        answer.append([prev_x, prev_y])
        return answer

a = Solution()
print(a.merge([[1, 4], [0, 4]]))
