import sys


def recur(wes, val, output):
    if len(wes) == 2:
        output.append(val)
        return
    for i in range(1, len(wes) - 1):
        new_wes = wes[:i] + wes[i + 1:]
        recur(new_wes, val + (wes[i - 1] * wes[i + 1]), output)


get_input = sys.stdin.readline

n = get_input()
weights = list(map(int, get_input().split()))

results = []
recur(weights, 0, results)

print(max(results))