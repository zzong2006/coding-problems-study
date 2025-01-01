import sys
from collections import deque, Counter


def solution():
    get_input = sys.stdin.readline
    long_str = get_input().strip()
    cnt = Counter()

    for ii in long_str:
        cnt[ii] += 1

    odd = 0
    even = 0
    odd_key = None
    for k in cnt.keys():
        if cnt[k] % 2 == 0:
            even += 1
        else:
            odd_key = k
            odd += 1
    if odd == 0 or odd == 1:
        ls = sorted(cnt.keys())
        ans = ""
        if odd == 0:
            for w in ls:
                ans += w * (cnt[w] // 2)
            ans = ans + ans[::-1]
            return ans
        else:
            for w in ls:
                ans += w * (cnt[w] // 2)

            ans = ans + odd_key + ans[::-1]
            return ans
    else:
        return "I'm Sorry Hansoo"


print(solution())
print("ABABA" < "BAAAB")
print("")
