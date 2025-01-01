# Definition for a binary tree node.
from collections import deque, defaultdict


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        dp = defaultdict(int)
        bin_val = bin(n)[2:]
        lo = len(bin_val)
        stack = deque()
        stack.append([bin_val, 0])
        dp[n] = 0
        goal = "0" * lo
        while stack:
            bin_str, op_v = stack.pop()
            if bin_str == goal:
                dp[goal] = op_v
                continue

            copied_str = bin_str[: lo - 1] + str(int(bin_str[-1]) ^ 1)
            val_ver = int(copied_str, 2)
            if val_ver not in dp or dp[val_ver] > op_v + 1:
                dp[val_ver] = op_v + 1
                stack.append([copied_str, op_v + 1])
            prev = bin_str[-1]
            idx = -1
            for i in reversed(range(len(bin_str) - 1)):
                if prev == "0":
                    if i == 0 and bin_str[i] == 1:
                        prev = bin_str[i]
                elif prev == "1":  # prev == 1
                    if bin_str[i] == "1":
                        idx = i + 1
                    break
            if idx != -1:
                # copied_str = bin_str[:]
                # print(bin_str[:idx - 1], bin_str[idx:])
                copied_str = (
                    bin_str[: idx - 1] + str(int(bin_str[idx]) ^ 1) + bin_str[idx:]
                )
                val_ver = int(copied_str, 2)
                if val_ver not in dp or dp[val_ver] > op_v + 1:
                    dp[val_ver] = op_v + 1
                    stack.append([copied_str, op_v + 1])
        print(dp)
        return dp[goal]


a = Solution()
print(a.minimumOneBitOperations(9))
