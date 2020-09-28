from collections import deque
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        ls = []

        waiting = 0  # 라인 기다리는 사람
        curr = 0  # 현재 곤돌라에 타고있는 사람
        days = 0
        max_profit = -1
        max_days = 0
        while days < len(customers) or waiting > 0 :
            if days < len(customers):
                waiting += customers[days]
            on_board = min(waiting, 4)
            waiting = max(waiting - 4, 0)
            curr += on_board
            profit = curr * boardingCost - (days + 1) * runningCost
            if max_profit < profit:
                max_days = days + 1
                max_profit = profit
            days += 1

        if max_profit < 0:
            return -1
        else:
            return max_days

a = Solution()
print(a.minOperationsMaxProfit([10, 10, 6, 4, 7], 3, 8))
