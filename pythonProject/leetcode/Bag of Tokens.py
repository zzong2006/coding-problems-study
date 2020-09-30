from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        a = 0
        b = len(tokens) - 1
        point = 0
        tokens.sort()
        if tokens:
            while a < b:
                if P > tokens[a]:
                    P -= tokens[a]
                    a += 1
                    point += 1
                else:
                    if point > 0:
                        P += tokens[b]
                        b -= 1
                        point -= 1
                    else:
                        return 0
            if a == b:
                if P >= tokens[a]:
                    return point + 1
                else:
                    return point
        else:
            return 0


a = Solution()
print(a.bagOfTokensScore([71, 55, 82], 54))
