import sys
import heapq
from collections import deque, defaultdict


class Tr:
    def __init__(self):
        self.pan = defaultdict(Tr)
        self.end = False

    def insert(self, word):
        curr = self
        for w in word:
            curr = curr.pan[w]
        curr.end = True

    def count_all(self):
        def dfs(curr_count, curr):
            t = 0
            ls = list(curr.pan.keys())
            if curr.end:
                t += curr_count
                if len(ls) >= 1:
                    for k in ls:
                        t += dfs(curr_count + 1, curr.pan[k])
            else:
                for k in ls:
                    if len(ls) > 1:
                        t += dfs(curr_count + 1, curr.pan[k])
                    else:
                        t += dfs(curr_count, curr.pan[k])
            return t

        total = 0
        for i in self.pan.keys():
            total += dfs(1, self.pan[i])

        return total


def solution():
    get_input = sys.stdin.readline

    while True:
        trie = Tr()
        h = get_input().strip()
        if h != '':
            n = int(h)
            names = []
            for i in range(n):
                names.append(get_input().strip())
                trie.insert(names[-1])
            total = trie.count_all()
            print('{:.2f}'.format(total / len(names)))
        else:
            break


solution()
