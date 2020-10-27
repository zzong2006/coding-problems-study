import sys
from collections import deque, Counter


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    answer = 1
    other = 1
    for i in range(m + 1):
        if i != m :
            answer *= (n - i)
        if i != 0:
            other *= i

    return answer // other

print(solution())
