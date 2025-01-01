from collections import deque
from sys import maxsize


def one_diff(a, b):
    idx = -1
    for i in range(len(a)):
        if a[i] != b[i] and idx == -1:
            idx = i
        elif a[i] != b[i] and idx != -1:
            return -2
    return idx


def solution(begin, target, words):
    answer = maxsize
    check = []
    que = deque()
    visited = set()
    visited.add(begin)
    que.append([begin, 0, words])

    if_if = False
    for wo in words:
        if wo == target:
            if_if = True
            break
    if not if_if:
        return 0

    while len(que) > 0:
        curr, cnt, words_list = que.popleft()
        if curr == target:
            answer = min(answer, cnt)
        elif cnt < answer:
            for i in range(len(words_list)):
                if one_diff(curr, words_list[i]) >= 0:
                    if i == 0:
                        new_list = words_list[i + 1 :]
                    else:
                        new_list = words_list[:i] + words_list[i + 1 :]
                    que.append([words_list[i], cnt + 1, new_list])

    return answer


print(solution("hit", "cog", ["hot", "dot", "lot", "dog", "cog", "log"]))
