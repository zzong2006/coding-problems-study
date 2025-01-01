from collections import Counter

import sys

get_input = sys.stdin.readline


def solution():
    def check(s):
        stack = []
        for x in s:
            if stack:
                if x == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(x)
            else:
                stack.append(x)
        if len(stack) == 0:
            return True
        else:
            return False

    n = int(get_input())
    for i in range(n):
        input_str = get_input().strip()
        if check(input_str):
            print("YES")
        else:
            print("NO")


solution()
