import bisect


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) > 0 and len(matrix[0]) > 0:
            start = 0
            end = len(matrix)
            idx = None
            if len(matrix) > 1:
                while start < end:
                    mid = (start + end) // 2
                    if matrix[mid][0] == target:
                        return True
                    elif matrix[mid][0] < target:
                        start = mid + 1
                    else:
                        end = mid

                if 0 <= end < len(matrix) and matrix[end][0] < target:
                    idx = end
                else:
                    idx = end - 1
            else:
                idx = 0
            # print(idx)

            ans_idx = bisect.bisect_left(matrix[idx], target)
            n = len(matrix[idx])
            if 0 <= ans_idx < n and matrix[idx][ans_idx] == target:
                return True
            else:
                return False
        else:
            return False


a = Solution()
# print(a.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 2))
print(a.searchMatrix([[1], [3]], 4))
