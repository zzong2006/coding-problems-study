import sys
from collections import Counter, defaultdict, deque


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
        curr.end = True

    def print_all(self):
        que = deque()
        for name in sorted(self.stem.keys()):
            self.dfs(name, self.stem[name], 0)

    def dfs(self, name, curr, lvl):
        print(("--" * lvl + name))
        for name in sorted(curr.stem.keys()):
            self.dfs(name, curr.stem[name], lvl + 1)


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    trie = Tron()
    for i in range(n):
        ls = get_input().strip().split()
        ls = ls[1:]
        trie.go_into(ls)
    trie.print_all()


solution()
