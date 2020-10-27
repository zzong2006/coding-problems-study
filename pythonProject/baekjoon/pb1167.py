import sys


def solution():
    def dfs(curr, dist, visited):
        for w, k in links[curr]:
            if w not in visited:
                memo[w] = dist + k
                visited.add(w)
                dfs(w, dist + k, visited)
                visited.remove(w)

    get_input = sys.stdin.readline
    n = int(get_input().strip())
    links = [list() for _ in range(n + 1)]
    for i in range(n):
        arr = list(map(int, get_input().strip().split()))
        # print(arr)
        for j in range(1, len(arr) - 1, 2):
            links[arr[0]].append((arr[j], arr[j + 1]))
    memo = [0] * (n + 1)

    for a, b in links[1]:
        memo[a] = b
        dfs(a, b, {a, 1})
    # argmax
    arg_idx = 0
    max_val = 0
    for i in range(1, len(memo)):
        if memo[i] > max_val:
            max_val = memo[i]
            arg_idx = i
    memo = [0] * (n + 1)
    # print(arg_idx)
    for a, b in links[arg_idx]:
        memo[a] = b
        dfs(a, b, {a, arg_idx})
    # print(memo)
    return max(memo)


print(solution())
