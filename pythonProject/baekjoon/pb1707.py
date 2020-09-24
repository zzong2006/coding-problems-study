import sys
from collections import deque
import heapq

get_input = sys.stdin.readline

t_c = int(get_input().strip())

for i in range(t_c):
    v, e = list(map(int, get_input().split()))
    vert = [0] * (v + 1)
    adj = [[] for _ in range(v + 1)]
    real_done = [False] * (v + 1)
    que = deque()

    for k in range(e):
        a, b = list(map(int, get_input().split()))
        adj[a].append(b)
        adj[b].append(a)

    for k in range(1, v + 1):
        vert[k] = 'b'
        que.append([k, (1 << k)])

    while len(que) >= 1:
        a, visited = que.pop()

        for k in adj[a]:
            if (1 << k) & visited <= 0 and real_done[k] is False:
                if vert[a] == 'b':
                    vert[k] = 'r'
                else:
                    vert[k] = 'b'
                real_done[k] = True
                que.append([k, visited + (1 << k)])


    no = False
    for z in range(1, v + 1):
        for k in adj[z]:
            if vert[z] == vert[k] and z != k:
                no = True
                break
        if no:
            break
    if no:
        print("NO")
    else:
        print("YES")
