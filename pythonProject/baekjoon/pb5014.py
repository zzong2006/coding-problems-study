import sys
from collections import deque

def recur(dyna, curr, goal, upper, up, down):
    que = deque()
    que.append([curr, 0])

    while len(que) > 0:
        curr, count = que.popleft()
        if curr == goal:
            return
        for x in [up, -down]:
            new_curr = curr + x
            if 1 <= new_curr <= upper and dyna[new_curr] > count + 1:
                dyna[new_curr] = count + 1
                que.append([new_curr, count + 1])


get_input = sys.stdin.readline

F, S, G, U, D = list(map(int, get_input().split()))

# S -> G
dp = [sys.maxsize] * (1000000 + 1)

recur(dp, S, G, F, U, D)

if S == G:
    print(0)
else:
    if dp[G] != sys.maxsize:
        print(dp[G])
    else:
        print('use the stairs')