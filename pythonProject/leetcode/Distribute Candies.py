from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType)
        if len(candy_set) <= len(candyType) // 2:
            return len(candy_set)
        else:
            ordered_candy = sorted(candy_set, reverse=True)
            return len(ordered_candy[: len(candyType) // 2])


solution = Solution()
solution.distributeCandies()
