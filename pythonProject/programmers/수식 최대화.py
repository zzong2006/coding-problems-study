from collections import deque
from itertools import combinations, permutations


def solution(expression):
    def do_cal(aa, bb, opp):
        if opp == '*':
            return aa * bb
        if opp == '-':
            return aa - bb
        if opp == '+':
            return aa + bb

    answer = 0
    que = deque()
    num = ""
    for i in expression:
        if '0' <= i <= '9':
            num += i
        else:
            que.append(int(num))
            que.append(i)
            num = ""
    que.append(int(num))

    for perm in permutations(['*', '-', '+']):
        new_que = que.copy()
        for target_op in perm:
            temp_que = deque()
            while new_que:
                it = new_que.popleft()
                if it == target_op:
                    a = temp_que.pop()
                    b = new_que.popleft()
                    temp_que.append(do_cal(a, b, it))
                else:
                    temp_que.append(it)
            new_que = temp_que.copy()
        assert len(new_que) == 1
        answer = max(answer, abs(new_que[0]))

    return answer


print(solution("100-200*300-500+20"))
