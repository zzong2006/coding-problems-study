import sys
from collections import deque

#  O(n log n) algorithm for suffix array construction


def solution():
    get_input = sys.stdin.readline
    ip_string = get_input().strip()
    ls = []
    for i in reversed(range(1, len(ip_string) + 1)):
        ls.append((ip_string[i - 1 :], i))
    ls.sort(key=lambda x: x[0])

    lcp = ["x"]
    for i in range(1, len(ls)):
        a = ls[i - 1][0]
        b = ls[i][0]
        curr = 0
        while curr < len(a) and curr < len(b):
            if a[curr] == b[curr]:
                curr += 1
            else:
                break
        lcp.append(curr)
    for i in range(len(ls)):
        print(ls[i][1], end=" ")
    print()
    for i in range(len(lcp)):
        print(lcp[i], end=" ")
    print()
    # print(lcp)


solution()
