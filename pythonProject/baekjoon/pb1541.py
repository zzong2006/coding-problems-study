import sys
from itertools import permutations

get_input = sys.stdin.readline
a = get_input().strip()

curr = 0
saved = 0
minus_start = False
bag = 0
for i in range(len(a)):
    if a[i] == "-" or a[i] == "+":
        if not minus_start and a[i] == "+":
            saved += int(a[curr : curr + (i - curr)])
            curr = i + 1
        elif not minus_start and a[i] == "-":
            saved += int(a[curr : curr + (i - curr)])
            curr = i + 1
            minus_start = True
            bag = 0
        elif minus_start and a[i] == "+":
            saved -= int(a[curr : curr + (i - curr)])
            curr = i + 1
        elif minus_start and a[i] == "-":
            saved -= int(a[curr : curr + (i - curr)])
            curr = i + 1
if not minus_start:
    saved += int(a[curr : curr + (i - curr + 1)])
else:
    saved -= int(a[curr : curr + (i - curr + 1)])
print(saved)
