class Solution:
    def maxPower(self, s: str) -> int:
        graphs = [[0] * (2 * (10 ** 4)) for _ in range(2 * (10 ** 4))]
        print(len(graphs[0]))
        start = 0
        end = 0
        answer = 1
        while start < len(s) - 1:
            one = s[start]
            lent = 1
            for i in range(start + 1, len(s)):
                if one != s[i]:
                    start += 1
                    break
                else:
                    lent += 1
                    start += 1

            answer = max(answer, lent)
        return answer


print(Solution().maxPower('leetcode'))