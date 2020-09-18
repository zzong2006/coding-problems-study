def solution(routes):
    routes.sort(key=lambda x: (x[0], x[1]))
    answer = 0
    left, right = routes[0]
    answer += 1
    for i in range(1, len(routes)):
        l, r = routes[i]
        if not (right < l or r < left):
            left = max(left, l)
            right = min(right, r)
        else:
            answer += 1
            left = l
            right = r

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))
