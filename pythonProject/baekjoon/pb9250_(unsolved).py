import sys
import heapq
from collections import defaultdict


class Tron:
    def __init__(self):
        self.m = dict()
        self.end = False

    def go_into(self, inp_st):
        curr = self
        for i in inp_st:
            if i not in curr.m:
                curr.m[i] = Tron()
            curr = curr.m[i]
        curr.end = True

    def search(self, inp_st):
        curr = self
        for i in inp_st:
            if curr.end is True:
                return True
            if i in curr.m:
                curr = curr.m[i]
            else:
                return False
        if curr.end is True:
            return True
        else:
            return False


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    trie = Tron()
    for i in range(n):
        st = get_input().strip()
        trie.go_into(st)
    k = int(get_input().strip())
    for k in range(k):
        st = get_input().strip()
        for i in range(len(st) - 1):
            if trie.search(st[i:]):
                print("YES")
                break
        else:
            print("NO")


solution()
