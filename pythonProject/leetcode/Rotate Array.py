class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(nums)
        n = len(nums)
        k %= n
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]
        print(nums)
        for i in range(k // 2):
            nums[i], nums[k - i - 1] = nums[k - i - 1], nums[i]
        print(nums)

        for i in range(k, (n + k - 1) // 2 + 1):
            nums[i], nums[n - i + k - 1] = nums[n - i + k - 1], nums[i]
        print(nums)


a = Solution()
a.rotate([1, 2, 3, 4, 5, 6, 7, 8, 9], k=3)
