import collections
from typing import List
import bisect

"""
아래는 내가 작성한 코드
"""
# class Solution:
#     def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
#         A.sort()
#         answer = []
#         for b in B:
#             idx = bisect.bisect_left(A, b)
#             print(idx, A, b)
#             for i in range(idx, len(A)):
#                 if A[i] > b:
#                     answer.append(A[i])
#                     A.pop(i)
#                     break
#             else:
#                 answer.append(A[0])
#                 A.pop(0)
#         return answer

"""
lee215의 코드
"""
class Solution:
    def advantageCount(self, A, B):
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]:
                take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]

a = Solution()
print(a.advantageCount([12,24,8,32], [13,25,32,11]))