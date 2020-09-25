from itertools import combinations

def solution(v):
    min_y = min([r[0] for r in v])
    max_y = max([r[0] for r in v])
    min_x = min([r[1] for r in v])
    max_x = max([r[1] for r in v])

    answer = []
    if [min_y, min_x] not in v:
        answer = [min_y, min_x]
    elif [min_y, max_x] not in v:
        answer = [min_y, max_x]
    elif [max_y, max_x] not in v:
        answer = [max_y, max_x]
    elif [max_y, min_x] not in v:
        answer = [max_y, min_x]

    return answer

print(solution([[1, 4], [3, 4], [3, 10]]))
