from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter()
        stack = list()
        visited = set()
        for i in range(len(s)):
            cnt[s[i]] += 1
        sorted_list = sorted(list(cnt.keys()))
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
                visited.add(s[i])
                cnt[s[i]] -= 1
            else:
                if s[i] not in visited:
                    while stack and stack[-1] > s[i] and cnt[stack[-1]] >= 1:
                        k = stack.pop()
                        visited.remove(k)
                    stack.append(s[i])
                    visited.add(s[i])
                cnt[s[i]] -= 1
        print(stack)
        return ''.join(stack)

a = Solution()
print(a.removeDuplicateLetters("edebbed"))
# expected: acdb

# acdb