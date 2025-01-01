from collections import deque
import heapq


def solution(operations):
    test = deque()

    answer = []
    for i in range(len(operations)):
        cmd = operations[i]
        if cmd[0] == "I":
            num = int(cmd[2:])
            test.append(num)
        else:
            if len(test) > 0:
                num = int(cmd[2:])
                test = deque(sorted(test))
                if num < 0:
                    test.popleft()
                else:
                    test.pop()
    test = deque(sorted(test))
    if len(test) > 0:
        answer.append(test[-1])
        answer.append(test[0])
    else:
        answer = [0, 0]
    # print(test)
    return answer


print(solution(["D 1", "D -1", "I -45", "I 45", "I 45", "D -1", "D 1"]))
