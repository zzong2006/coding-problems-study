from collections import deque
import sys


def solution():
    get_input = sys.stdin.readline
    a, b = list(map(int, get_input().strip().split()))
    first = list(map(int, get_input().strip().split()))
    second = list(map(int, get_input().strip().split()))
    answer = []
    a_idx = 0
    b_idx = 0
    while a_idx < len(first) and b_idx < len(second):
        if first[a_idx] <= second[b_idx]:
            answer.append(first[a_idx])
            a_idx += 1
        else:
            answer.append(second[b_idx])
            b_idx += 1
    while a_idx < len(first):
        answer.append(first[a_idx])
        a_idx += 1
    while b_idx < len(second):
        answer.append(second[b_idx])
        b_idx += 1

    print(" ".join(list(map(str, answer))))


solution()
