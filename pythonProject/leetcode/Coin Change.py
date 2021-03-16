from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)

        def get_results(curr_amount, curr_idx, res):
            if curr_amount == 0:
                return res
            else:
                for k in range(curr_idx, len(coins)):
                    val = coins[k]
                    if curr_amount >= val:
                        ww = curr_amount // val
                        result = get_results(curr_amount - ww * val, k + 1, res + ww)
                        if result != -1:
                            return result
                return -1

        res = -1
        for w in range(len(coins)):
            res = get_results(amount, w, 0)
            if res != -1:
                break
        return res


a = Solution()
print(a.coinChange([186, 419, 83, 408], 6249))
