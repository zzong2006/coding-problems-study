import sys
from itertools import permutations

get_input = sys.stdin.readline

a, b = list(map(int,get_input().strip().split()))

for x in permutations(range(1, a +1 ), b):
    for j in x:
        print(j, end=" ")
    print()