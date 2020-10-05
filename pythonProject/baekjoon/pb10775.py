import sys


def solution():
    def find(x):
        p = ls[x]
        if p != x:
            r = find(p)
            ls[x] = r
            return ls[x]
        return p

    def union(a, b):
        x = find(a)
        y = find(b)
        if x != y:
            if x < y:
                ls[y] = x
            else:
                ls[x] = y

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    ls = [i for i in range(n + 1)]
    p = int(get_input().strip())
    count = 0
    for i in range(p):
        z = int(get_input().strip())
        val = find(z)
        if val != 0:
            union(val - 1, z)
            count += 1
        else:
            break
    print(count)


solution()
