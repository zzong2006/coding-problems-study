def solution(n, computers):
    def dfs(curr):
        if curr not in visited:
            visited.add(curr)
            for i in range(n):
                if i != curr and computers[i][curr] or computers[curr][i] and i not in visited:
                    dfs(i)

    visited = set()
    answer = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            answer += 1

    return answer


print(solution(	3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))