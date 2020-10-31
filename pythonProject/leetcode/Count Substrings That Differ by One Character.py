class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def check_diff(a, b):
            assert len(a) == len(b)
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
            return count

        memo = dict()
        answer = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub_str = s[i:j]
                if sub_str in memo:
                    answer += memo[sub_str]
                else:
                    n = len(sub_str)
                    total_cnt = 0
                    for k in range(len(t) - n + 1):
                        cnt = check_diff(sub_str, t[k:k + n])
                        if cnt == 1:
                            # print(sub_str, t[k:k+n])
                            total_cnt += 1
                    memo[sub_str] = total_cnt
                    answer += total_cnt
        return answer


a = Solution()
print(a.countSubstrings("a", "a"))
