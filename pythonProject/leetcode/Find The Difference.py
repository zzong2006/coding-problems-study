class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = [0] * 27
        for i in s:
            count_s[ord(i) - ord('a')] += 1

        count_t = [0] * 27
        for j in t:
            count_t[ord(j) - ord('a')] += 1

        for k in range(len(count_s)):
            if count_s[k] - count_t[k] != 0:
                return chr(k + ord('a'))

a = Solution()
print(a.findTheDifference("abcd","abcde"))