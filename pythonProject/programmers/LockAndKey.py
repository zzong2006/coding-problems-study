from collections import deque
import timeit

def rotate(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]

    for i in range(len(a)):
        for j in range(len(a[0])):
            new_key[i][j] = a[j][len(a[0]) - i - 1]
    return new_key


def fit(k, lo, s_of_z):
    if len(k) < len(lo):
        n = len(lo)
        m = len(k)
        x_step = 0
        y_step = 0
        trials = []
        while y_step <= n - m:
            hap = 0
            zero_count = 0
            for i in range(len(k)):
                for j in range(len(k[0])):
                    hap += k[i][j] ^ lo[i + y_step][j + x_step]
                    if lo[i + y_step][j + x_step] == 0:
                        zero_count += 1
            if hap == m * m and zero_count == s_of_z:
                return True
            else:
                x_step += 1
                if x_step > (n - m):
                    y_step += 1
                    x_step = 0
        return False
    else:
        for i in range(len(k)):
            for j in range(len(k[0])):
                if abs(k[i][j] - 1) != lo[i][j]:
                    return False
    return True


def move_up(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(0, len(a) - 1):
        new_key[i][:] = a[i + 1][:]
    return new_key


def move_down(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(1, len(a)):
        new_key[i][:] = a[i - 1][:]
    return new_key


def move_left(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0]) - 1):
            new_key[i][j] = a[i][j + 1]
    return new_key


def move_right(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(1, len(a[0])):
            new_key[i][j] = a[i][j - 1]
    return new_key


def solution(key, lock):
    # count whole 0 from lock
    sum_of_zero = 0
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                sum_of_zero += 1
    que = deque()
    answer = False
    key = tuple(map(tuple, key))
    que.append((key, 0))
    check = set()
    check.add(key)

    while len(que) > 0 or answer:
        kk, angle = que.popleft()
        if fit(kk, lock, sum_of_zero):
            # print(kk, lock)
            return True
        else:
            # up , down, right, left
            up_key = move_up(kk)
            tp = tuple(map(tuple, up_key))
            sum_of_ones = sum(list(map(sum,tp)))
            if tp not in check and sum_of_ones >= sum_of_zero:
                check.add(tp)
                que.append((tp, angle))

            down_key = move_down(kk)
            tp = tuple(map(tuple, down_key))
            sum_of_ones = sum(list(map(sum, tp)))
            if tp not in check and sum_of_ones >= sum_of_zero:
                check.add(tp)
                que.append((tp, angle))

            right_key = move_right(kk)
            tp = tuple(map(tuple, right_key))
            sum_of_ones = sum(list(map(sum, tp)))
            if tp not in check and sum_of_ones >= sum_of_zero:
                check.add(tp)
                que.append((tp, angle))

            left_key = move_left(kk)
            tp = tuple(map(tuple, left_key))
            sum_of_ones = sum(list(map(sum, tp)))
            if tp not in check and sum_of_ones >= sum_of_zero:
                check.add(tp)
                que.append((tp, angle))

            if angle < 270 :
                rotate_key = rotate(kk)
                tp = tuple(map(tuple, rotate_key))
                sum_of_ones = sum(list(map(sum, tp)))
                if tp not in check and sum_of_ones >= sum_of_zero:
                    check.add(tp)
                    que.append((tp, angle + 90))

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]))
