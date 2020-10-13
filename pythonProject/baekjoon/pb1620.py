import sys
from collections import deque


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    num_dict = dict()
    str_dict = dict()

    for i in range(n):
        name = get_input().strip()
        str_dict[name] = i + 1
        num_dict[i + 1] = name
    for i in range(m):
        name = get_input().strip()
        if name[0].isalpha():
            print(str_dict[name])
        else:
            print(num_dict[int(name)])


solution()
