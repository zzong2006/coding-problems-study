class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        if arr:
            arr.sort()
            n = len(arr)
            start = int(n * 0.05)
            end = int(n * 0.95)
            print(start, end)
            return sum(arr[start:end]) / (end - start)
        else:
            return 0


a = Solution()
# print(a.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 2))
print(a.trimMean(
    [6, 0, 7, 0, 7, 5, 7, 8, 3, 4, 0, 7, 8, 1, 6, 8, 1, 1, 2, 4, 8, 1, 9, 5, 4, 3, 8, 5, 10, 8, 6, 6, 1, 0, 6, 10, 8, 2,
     3, 4]))
print((1, 2) < (2, 3))
