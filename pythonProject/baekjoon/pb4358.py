import sys
from collections import Counter


def solution():
    get_input = sys.stdin.readline
    tree_list = Counter()
    a = get_input().strip()
    tree_list[a] += 1
    total = 1
    while a:
        a = get_input().strip()
        if a:
            tree_list[a] += 1
            total += 1
    ls = list(tree_list.keys())
    ls.sort()
    for name in ls:
        print("{} {:.4f}".format(name, tree_list[name] / total * 100.0))
    # print(tree_list)


solution()
