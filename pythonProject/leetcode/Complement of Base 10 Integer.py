class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        a = bin(N)
        answer = ""
        for i in range(2, len(a)):
            ch = a[i]
            if ch == '0':
                answer += '1'
            else:
                answer += '0'
        return int(answer, 2)

kk = Solution()
print(kk.bitwiseComplement(6))