from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        else:
            tank = 0
            start_idx = 0
            for i in range(len(gas)):
                tank += (gas[i] - cost[i])

                if tank < 0:
                    start_idx = i + 1
                    tank = 0
                    continue

            return start_idx

s = Solution()
print(s.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))
