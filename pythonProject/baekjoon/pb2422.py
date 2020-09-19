from itertools import combinations

n, m = list(map(int, input().split()))
combs = []
combs = list(combinations(range(1, n + 1), 3))

ices = [[False] * (n + 1) for _ in range(n + 1)]
ans = []
no_combs = {}
for i in range(m):
    a = list((map(int, input().split())))
    ices[a[0]][a[1]] = True
    ices[a[1]][a[0]] = True

count = 0
for a, b, c in combs:
    if not ices[a][b] and not ices[b][c] and not ices[a][c]:
        count += 1

print(count)
