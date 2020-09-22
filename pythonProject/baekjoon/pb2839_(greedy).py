# greedy 버전으로 푼 문제

import sys

get_input = sys.stdin.readline

n = int(get_input().strip())

remains = n % 5
five = n // 5

while five >= 0:
    if remains % 3 == 0:
        three = remains // 3
        print(three + five)
        break
    else:
        remains += 5
        five -= 1
if five < 0:
    print(-1)