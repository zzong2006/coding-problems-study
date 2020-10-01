import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    ip_string = get_input().strip()
    ls = []
    for i in reversed(range(1, len(ip_string) + 1)):
        ls.append((ip_string[i-1:], i))
    ls.sort(key=lambda x:x[0])


    for i in range(len(ls)):
        print(ls[i][0])


    # print(lcp)
solution()