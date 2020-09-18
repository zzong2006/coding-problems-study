def solution(n, results):
    check = [[set() for _ in range(2)] for _ in range(n + 1)]
    # x -> y ( x beats y)
    # 0 -> / 1 <-
    for x, y in results:
        check[x][0].add(y)
        check[y][1].add(x)

    queue = []
    for i in range(n):
        if len(check[i + 1][0]) == 0:
            queue.append(([], i + 1))

    visited = [-1] * (n + 1)

    while queue:
        ls, num = queue.pop(0)
        for a in ls:
            check[num][0].add(a)
            check[a][1].add(num)
        for j in check[num][1]:
            if visited[j] <= len(ls):
                queue.append((ls + [num], j))
                visited[j] = len(ls)

    answer = 0
    for i in range(len(check)):
        if len(check[i][0]) + len(check[i][1]) == n - 1:
            answer += 1

    return answer


print(solution(8, [[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]]))
