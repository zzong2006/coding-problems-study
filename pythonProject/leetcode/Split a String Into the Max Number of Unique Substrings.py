class Solution:
    test = [1]

    def maxUniqueSplit(self, s: str) -> int:
        self.test = [1]
        self.recur(set(), 0, s)
        return max(self.test)

    def recur(self, words: set, idx, string):
        if idx == len(string):
            # print(words)
            self.test.append(len(words))
        else:
            for i in range(0, len(string) - idx + 1):
                word = string[idx : idx + i]
                if word == "":
                    continue
                if word in words:
                    continue
                else:
                    new_words = words.copy()
                    new_words.add(word)
                    self.recur(new_words, idx + i, string)


a = Solution()
print(a.maxUniqueSplit("hmadataa"))
print(a.maxUniqueSplit("aa"))
