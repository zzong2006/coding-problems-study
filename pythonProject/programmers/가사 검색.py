from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 7)


class Tr:
    def __init__(self):
        self.book = defaultdict(Tr)
        self.length = 0
        self.end = False

    def insert(self, word):
        curr = self
        for w in word:
            curr.length += 1
            if w not in curr.book:
                curr.book[w] = Tr()
            curr = curr.book[w]
        curr.end = True


def solution(words, queries):
    def search(idx, query, curr):
        if idx < len(query):
            result = 0
            if query[idx] == '?':
                if curr.length is None:
                    for k in curr.book.keys():
                        result += search(idx + 1, query, curr.book[k])
                    curr.length = result
                else:
                    return curr.length
            else:
                if query[idx] in curr.book:
                    result += search(idx + 1, query, curr.book[query[idx]])
            return result
        else:
            if curr.end:
                return 1
            else:
                return 0

    answer = []
    main_trie = defaultdict(Tr)
    main_reverse_trie = defaultdict(Tr)
    for w in words:
        main_trie[len(w)].insert(w)
        main_reverse_trie[len(w)].insert(w[::-1])

    for q in queries:
        if q[0] == '?':
            output = search(0, q[::-1], main_reverse_trie[len(q)])
        else:
            output = search(0, q, main_trie[len(q)])
        answer.append(output)
    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["?????", "?f", "fro??", "????o", "??????", "fr???", "fro???", "pro?"]))
