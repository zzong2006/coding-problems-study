class Solution:
    def maxDepth(self, s: str) -> int:
        def go(other_s: str, count):
            other_max = 0
            for i in range(len(other_s)):
                if other_s[i] == ')':
                    return count
                elif other_s[i] == '(':
                    return go(other_s[i + 1:], count + 1)
            return other_max

        max_val = 0
        count = 0
        for ii in range(len(s)):
            if s[ii] == '(':
                count += 1
                max_val = max(max_val, go(s[ii + 1:], count))
            elif s[ii] == ')':
                count -= 1
        return max_val


a = Solution()
print(a.maxDepth("(1)+((2))+(((3)))"))
print(a.maxDepth("(1+(2*3)+((8)/4))+1"))