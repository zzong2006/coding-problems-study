from sys import stdin
from collections import deque
from itertools import combinations

N, K = list(map(int, stdin.readline().split()))
n_angles = list(map(int, stdin.readline().split()))
targets = list(map(int, stdin.readline().split()))


def check(angles, target):
    que = deque()
    angle_check = set()

    for i in range(len(angles)):
        angle_check.add(angles[i])
        angle_check.add(360 - angles[i])
        que.append(angles[i])
        que.append(360 - angles[i])

    while len(que) > 0:
        curr = que.popleft()
        if curr == target:
            return True
        else:
            for i in range(len(angles)):
                new_curr = (curr + angles[i]) % 360
                if new_curr not in angle_check:
                    angle_check.add(new_curr)
                    que.append(new_curr)
                new_curr = (curr - angles[i])
                if new_curr < 0:
                    new_curr = 360 + new_curr
                if new_curr not in angle_check :
                    angle_check.add(new_curr)
                    que.append(new_curr)
    return False


for k in targets:
    answer = False
    for i in range(1, len(n_angles) + 1):
        for x in combinations(n_angles, i):
            if check(x, k):
                answer = True
                print("YES")
                break
        if answer:
            break
    if not answer:
        print("NO")
