from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries :
            curr = timeSeries[0]
            will_end = curr + duration
            output = duration
            for i in range(1, len(timeSeries)):
                time = timeSeries[i]
                if time < will_end:
                    output = output + (time - curr)
                else:
                    output += duration
                curr = time
                will_end = time + duration
        else:
            output = 0
        return output

a = Solution()
print(a.findPoisonedDuration([1, 2, 3, 4, 5], 5))
