import time
start = time.time()  # 시작 시간 저장

N, K = list(map(int, input().split()))
"""
N K
문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.
"""

from itertools import combinations

done = False
ans = []


def recursive_helper(curr: str, total, num_of_b):
    if len(ans) <= 0:
        if len(curr) < N and total < K:
            recursive_helper("B" + curr, total, num_of_b + 1)
            recursive_helper("A" + curr, total + num_of_b, num_of_b)
        elif len(curr) == N and total == K:
            ans.append(curr)
            return curr


recursive_helper("", 0, 0)

if len(ans) > 0:
    print(ans[0])
else:
    print(-1)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
