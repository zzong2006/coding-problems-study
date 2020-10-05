import sys
from collections import Counter, defaultdict


def solution():
    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    arm = set()
    for i in range(n):
        arm.add(get_input().strip())
    count = 0

    cnt = Counter()
    for i in range(m):
        cnt[get_input().strip()] += 1
    bam = set(cnt.keys())
    result = arm.intersection(bam)
    for name in result:
        count += cnt[name]

    return count


print(solution())
