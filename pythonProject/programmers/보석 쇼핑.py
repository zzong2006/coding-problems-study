from collections import Counter


def solution(gems):
    def span(a: list):
        return a[1] - a[0]

    total = len(set(gems))
    n = len(gems)
    box = Counter()
    start = end = 1
    i = -1
    start = 0
    answer = None
    for j in range(n):
        if j > 0:
            box[gems[j - 1]] -= 1
            if box[gems[j - 1]] == 0:
                del box[gems[j - 1]]
        while i < n:
            if len(box) == total:
                break
            else:
                i += 1
                if i < n:
                    box[gems[i]] += 1
                if len(box) == total:
                    break
        else:
            break
        new_interval = [j + 1, i + 1]
        if answer is None:
            answer = new_interval.copy()
        else:
            if new_interval[0] <= new_interval[1] and span(new_interval) < span(answer):
                answer = new_interval.copy()

    return answer


print(solution(["B", "A", "A", "B", "B"]))
