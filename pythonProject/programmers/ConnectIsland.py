def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    answer = 0
    visited = [False] * n

    ls = [x for x in range(n)]

    for x, y, c in costs:
        if find(x, ls) != find(y, ls):
            answer += c
            union(x, y, ls)
        if check(ls):
            break
    return answer


def check(parents):
    if parents.count(parents[0]) == len(parents):
        return True
    else:
        return False


def union(y, x, parents):
    y = find(y, parents)
    x = find(x, parents)
    if y != x:
        parents[y] = x


def find(x, parents):
    y = parents[x]
    if y == x:
        return y
    else:
        p_of_y = find(y, parents)
        parents[x] = p_of_y
        return parents[x]


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
