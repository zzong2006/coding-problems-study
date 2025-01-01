"""
M과 N이 주어질 때 M이상 N이하의 자연수 중 완전제곱수인 것을 모두 골라 그 합을 구하고 그 중 최솟값을 찾는 프로그램을 작성하시오.
예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 완전제곱수는 64, 81, 100 이렇게 총 3개가 있으므로 그 합은 245가 되고 이 중 최솟값은 64가 된다.

M이상 N이하의 자연수 중 완전제곱수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
단, M이상 N이하의 자연수 중 완전제곱수가 없을 경우는 첫째 줄에 -1을 출력한다.
"""

import sys
import math

get_input = sys.stdin.readline

M = int(get_input())
N = int(get_input())

min_val = sys.maxsize
sum_val = 0
for i in range(M, N + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        min_val = min(min_val, i)
        sum_val += i

if min_val == sys.maxsize:
    print(-1)
else:
    print(sum_val)
    print(min_val)
