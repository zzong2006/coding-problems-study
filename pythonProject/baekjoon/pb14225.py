from itertools import combinations
import sys

get_input = sys.stdin.readline

"""
아래 코드는 다른 사람의 것 (Accepted, 약 100ms)
"""
len_s, s = int(sys.stdin.readline()), sorted([int(x) for x in sys.stdin.readline().split(' ')])
for i in range(len_s):
    if i == 0:
        if s[i] == 1:
            continue
        else:
            print(1)
            break
    if sum(s[:i]) + 1 < s[i]:
        print(sum(s[:i], 1))
        break
else:
    print(sum(s, 1))

"""
아래 코드는 나의 것 (Accepted, 약 1000ms)
"""
# n = int(get_input().strip())
#
# nums = list(map(int, get_input().split()))
# nums.sort()
# sums = set()
# for i in range(1, len(nums) + 1):
#     for perms in combinations(nums, i):
#         total = 0
#         for k in perms:
#             total += k
#         # print(perms, total)
#         sums.add(total)
#
# max_val = -1
# done = False
# a = list(sums)
# max_val = max(a)
# start = 1
# while start <= max_val:
#     if start not in sums:
#         print(start)
#         done = True
#         break
#     else:
#         start += 1
#
# if not done:
#     print(max_val + 1)
