import re
import sys
from collections import defaultdict


class Tron:
    def __init__(self):
        self.stem = defaultdict(Tron)
        self.end = False

    def go_into(self, input_str):
        curr = self
        for i in range(len(input_str)):
            ch = input_str[i]
            if ch not in curr.stem:
                curr.stem[ch] = self.__class__()
                curr = curr.stem[ch]
            else:
                curr = curr.stem[ch]
                if curr.end is True:
                    return False
        curr.end = True
        return True


def solution():
    get_input = sys.stdin.readline

    t = int(get_input().strip())
    for i in range(t):
        n = int(get_input().strip())
        trie = Tron()
        string_list = []
        for j in range(n):
            string_list.append(get_input().strip())
        string_list.sort(key=lambda x: len(x))
        for aa in string_list:
            if not trie.go_into(aa):
                print("NO")
                break
        else:
            print("YES")


solution()
