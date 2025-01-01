import sys
import heapq


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    ranks = list(map(int, get_input().strip().split()))
    result = 0
    while len(ranks) > 1:
        v = ranks[0]
        idx = 0
        for k in range(1, len(ranks)):
            if ranks[k] > v:
                v = ranks[k]
                idx = k

        if idx == 0:
            result += abs(ranks[idx] - ranks[idx + 1])
        elif idx == len(ranks) - 1:
            result += abs(ranks[idx - 1] - ranks[idx])
        else:
            left = abs(ranks[idx - 1] - ranks[idx])
            right = abs(ranks[idx + 1] - ranks[idx])
            if left < right:
                result += left
            else:
                result += right
        ranks.pop(idx)

    return result


print(solution())
