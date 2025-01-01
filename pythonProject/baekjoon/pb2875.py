"""
대회 or 인턴
"""

import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    std = get_input().strip()
    if std[-1] == "s":
        return std + "es"
    else:
        return std + "s"


print(solution())

# import sys
# from collections import deque
#
#
# def solution():
#     get_input = sys.stdin.readline
#     n, m, k = list(map(int, get_input().strip().split()))
#     male = 0
#     female = 0
#     count = 0
#     while male <= m and female <= n:
#         male += 1
#         female += 2
#         count += 1
#
#         if m - male + n - female < k:
#             break
#
#     return count - 1
#
#
# print(solution())
