from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        cnt = [0] * len(nums)
        answer = []
        for i in nums:
            cnt[i - 1] += 1
            if cnt[i - 1] > 1:
                answer.append(i)
        for j in range(len(cnt)):
            if cnt[j] <= 0:
                answer.append(j + 1)
                break
        return answer


