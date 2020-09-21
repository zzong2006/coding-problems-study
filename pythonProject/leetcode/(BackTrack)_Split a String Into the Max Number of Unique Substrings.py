class Solution:
    test = [1]

    def maxUniqueSplit(self, s: str) -> int:
        # self.test = [1]
        result = self.recur(s, set())
        return result

    def recur(self, s: str, win: set):
        max_val = 0

        for i in range(1, len(s) + 1):
            new_s = s[0:i]
            if new_s not in win:
                win.add(new_s)
                max_val = max(max_val, 1 + self.recur(s[i:], win))
                win.remove(new_s)

        return max_val


a = Solution()
print(a.maxUniqueSplit("ababccc"))
print(a.maxUniqueSplit("aa"))
