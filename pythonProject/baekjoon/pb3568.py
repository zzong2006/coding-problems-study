import sys
from collections import deque, defaultdict


def solution():
    get_input = sys.stdin.readline
    string_ring: str = get_input().strip()
    stacked = defaultdict(list)
    splinted = string_ring.split(",")
    data_type, rem = splinted[0].split(" ")
    splinted = [rem] + splinted[1:]
    for stirrer in splinted:
        name = ""
        stirrer = stirrer.strip()
        for i in stirrer:
            if i == "[" or i == "*" or i == "&":
                stacked[name].append(i)
            elif i != "]" and i != ";":
                name += i
        stacked[name]
    for i in stacked.keys():
        copied = data_type
        for j in stacked[i][::-1]:
            if j == "[":
                copied += "[]"
            else:
                copied += j

        print(copied, end=" ")
        print(i, end=";\n")


solution()
