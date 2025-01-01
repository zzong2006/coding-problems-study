from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ls = []
        for log in logs:
            if log[0] != ".":
                sp = log.split("/")
                ls.append(sp[0])
            elif log[0] == ".":
                if log[1] == ".":
                    if ls:
                        ls.pop()
        return len(ls)


a = Solution()
print(a.minOperations(["d1/", "../", "../", "../"]))
