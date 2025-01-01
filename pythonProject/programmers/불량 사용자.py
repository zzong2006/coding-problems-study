import re
from collections import defaultdict, deque
import itertools


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


def solution(user_id, banned_id):
    def get_combinations(curr_set, curr_ls):
        pass

    trie = Tron()

    for name in user_id:
        trie.go_into(name)
    que = deque()
    total_ls = []
    for name in banned_id:
        que.append((trie, 0, ""))
        ls = []
        while que:
            curr, idx, curr_str = que.popleft()
            if curr.end is True and len(curr_str) == len(name):
                ls.append(curr_str)
            if idx < len(name):
                ch = name[idx]
                if ch != "*" and ch in curr.stem:
                    que.append((curr.stem[ch], idx + 1, curr_str + ch))
                elif ch == "*":
                    for stem_ch in curr.stem.keys():
                        que.append((curr.stem[stem_ch], idx + 1, curr_str + stem_ch))
        total_ls.append(ls)
    answer = []
    print(total_ls)
    for pd in list(itertools.product(*total_ls)):
        set_pd = set(pd)
        if len(set_pd) == len(banned_id):
            for i in range(len(answer)):
                if answer[i] == set_pd:
                    break
            else:
                answer.append(set_pd)

    answer = len(answer)

    return answer


solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"],
)
