class Trie:
    def __init__(self):
        self.m = dict()

    def insert_val(self, val):
        curr = self

        for k in val:
            if k not in curr.m:
                curr.m[k] = Trie()
            curr = curr.m[k]

    def check_is_in(self, val):
        curr = self

        for k in val:
            if k not in curr.m:
                return False
            else:
                curr = curr.m[k]

        return True


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        root = Trie()

        for i in range(len(s) - k + 1):
            root.insert_val(s[i:i + k])

        result = True
        for w in range(2 ** k):
            result &= root.check_is_in(bin(w)[2:].zfill(k))
            if not result:
                break

        return result

a = Solution()
a.hasAllCodes("00110", 2)