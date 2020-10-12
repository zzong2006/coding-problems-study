from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        else:
            n = len(A)
            count = 0
            cnt = Counter()
            overlap = False
            diff = []
            for i in range(n):
                cnt[A[i]] += 1
                if cnt[A[i]] >= 2:
                    overlap = True
                if A[i] != B[i]:
                    count += 1
                    diff.append(i)
                if count > 2:
                    return False
            if count == 2:
                if A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
                    return True
            if count == 0 and overlap:
                return True
        return False

a = Solution()
print(a.buddyStrings("abcba", "abcab"))