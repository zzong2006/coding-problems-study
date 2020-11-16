#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
import bisect
from collections import Counter

def climbingLeaderboard(ranked, player):
    answer = []
    st = []
    new_ranked = []
    for r in ranked:
        if not new_ranked or new_ranked and new_ranked[-1] != r:
            new_ranked.append(r)
    # print(new_ranked)
    for p in player:
        start = 0
        end = len(new_ranked)
        while start < end:
            mid = (start + end) // 2
            if p < new_ranked[mid]:
                start = mid + 1
            else:
                end = mid
        # print(start)
        answer.append(start + 1)
    # print(answer)
    return answer


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)
