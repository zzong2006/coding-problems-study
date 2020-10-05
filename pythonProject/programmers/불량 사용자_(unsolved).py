import re
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
        curr.end = True


def solution(user_id, banned_id):
    trie = Tron()

    trie.go_into('hello')
    print(trie)
    answer = 0
    banned_id.sort(reverse=True)


    return answer


# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], 	["fr*d*", "abc1**"])
# solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], 	["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["******", "fr*d*", "*rodo", "******", "**"])
