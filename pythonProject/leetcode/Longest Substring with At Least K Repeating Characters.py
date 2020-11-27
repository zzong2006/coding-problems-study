from collections import Counter


class Solution:

    def __init__(self):
        self.output = 0

    def longestSubstring(self, s: str, k: int) -> int:
        def divided_conquer(curr_s):
            output = 0
            if curr_s:
                cnt = Counter(curr_s)
                for i in range(len(curr_s)):
                    if cnt[curr_s[i]] < k:
                        output = max(divided_conquer(curr_s[:i]), divided_conquer(curr_s[i + 1:]))
                        break
                else:
                    return max(output, len(curr_s))
            return output
        answer = divided_conquer(s)

        return answer


a = Solution()
print(a.longestSubstring('aaabb', 3))
