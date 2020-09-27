from collections import deque
from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        profit = 0
        waiting = 0
        on_board = 0
        que = deque()
        prev_profit = 0
        
        for i in range(len(customers)):
            customer = customers[i]
            waiting += customer
            if waiting > 4:
                waiting -= 4
                will_board = 4
            else:
                waiting = 0
                will_board = waiting
            que.append(will_board)
            on_board += will_board
            if len(que) > 4:
                out_num = que.popleft()
                on_board -= out_num
            profit += (boardingCost * on_board - runningCost * len(que))
            if i > 0 and profit < prev_profit:
                return i + 1
            else:
                prev_profit = profit

        return i + 1