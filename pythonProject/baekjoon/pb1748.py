import math
import sys


def solution():
    a = int(sys.stdin.readline().strip())
    if a <= 9:
        return a

    v = int(math.log10(a))
    k = 0
    for i in range(v + 1):
        if i != v:
            k += (i + 1) * (9 * (10**i))
        else:
            k += (i + 1) * (a - ((10**i) - 1))
    return k


print(solution())
