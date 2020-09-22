import sys
from math import log10

get_input = sys.stdin.readline
a = get_input().strip()

total = 0
target = [0] * 10
num = a
for i in a:
    j = int(i)
    total += j
    total %= 3
    target[j] += 1

answer = ""

if target[0] > 0 and total % 3 == 0 :
    curr = 9
    while curr >= 0 :
        if target[curr] > 0:
            answer += str(curr)
            target[curr] -= 1
        else:
            curr -= 1

    print(answer)
else:
    print(-1)