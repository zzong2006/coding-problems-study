from collections import deque
import sys

get_input = sys.stdin.readline

n = list(map(int, get_input().split()))[0]

start = []
for i in get_input().strip():
    start.append(int(i))

target = []
for i in get_input().strip():
    target.append(int(i))

s = set()
for i in range(n):
    if start[i] != target[i]:
        s.add(i)
done = False
if len(s) == 0:
    print(0)
    done = True

if not done:
    # 0 번 스위치를 눌렀을 때
    save_start = start[:]
    start[0] ^= 1
    if 0 in s:
        s.remove(0)
    else:
        s.add(0)
    start[1] ^= 1
    if 1 in s:
        s.remove(1)
    else:
        s.add(1)
    switch = 1


    for i in range(1, n):
        if start[i - 1] != target[i - 1]:
            if i == n - 1:
                for k in [i, i - 1]:
                    if k in s:
                        s.remove(k)
                    else:
                        s.add(k)
                    start[k] ^= 1
            else:
                for k in [i, i - 1, i + 1]:
                    if k in s:
                        s.remove(k)
                    else:
                        s.add(k)
                    start[k] ^= 1
            switch += 1
        else:  # check
            if len(s) == 0:
                print(switch)
                done = True
                break
if not done:
    if len(s) == 0:
        print(switch)
        done = True


if not done:
    # 0 번 스위치를 누르지 않았을 때
    start = save_start[:]
    s.clear()
    for i in range(n):
        if start[i] != target[i]:
            s.add(i)
    switch = 0
    done = False

    for i in range(1, n):
        if start[i - 1] != target[i - 1]:
            if i == n - 1:
                for k in [i, i - 1]:
                    if k in s:
                        s.remove(k)
                    else:
                        s.add(k)
                    start[k] ^= 1
            else:
                for k in [i, i - 1, i + 1]:
                    if k in s:
                        s.remove(k)
                    else:
                        s.add(k)
                    start[k] ^= 1
            switch += 1
        else:  # check
            if len(s) == 0:
                print(switch)
                done = True
                break
if not done:
    if len(s) == 0:
        print(switch)
        done = True
    else:
        print(-1)
