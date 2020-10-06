import sys


def solution():
    def union(x, y):
        x = find(x)
        y = find(y)
        if x != y:
            ls[x] = y

    def find(t):
        x = ls[t]
        if x != t:
            y = find(x)
            ls[t] = y
            return ls[t]
        return ls[t]

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    b = int(get_input().strip())
    ls = list(range(n))
    for i in range(n):
        net = list(map(int, get_input().strip().split()))
        for k in range(n):
            if i != k and net[k]:
                union(i, k)
    travel = list(map(int, get_input().strip().split()))
    curr = find(travel[0] - 1)

    for i in range(1, len(travel)):
        if find(travel[i] - 1) != curr:
            print("NO")
            break
        curr = find(travel[i] - 1)
    else:
        print("YES")


solution()
