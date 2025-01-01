from collections import Counter
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def recur(curr, ls, idx):
            # print(ls)
            if curr == target:
                answer.append(ls)
            elif curr > target:
                return
            else:
                for i in range(idx, len(candidates)):
                    recur(curr + candidates[i], ls + [candidates[i]], i)

        candidates.sort()
        visited = set()
        answer = []
        for idx, n in enumerate(candidates):
            recur(n, [n], idx)
        return answer


a = Solution()
print(a.combinationSum([2, 3, 6, 7], 7))
