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
    n = len(a)
    new_key = [[0] * n for _ in range(len(a[0]))]
    removed_ones = sum(a[n - 1][:])
    for i in range(0, n - 1):
        if i < n - 1:
            new_key[i][:] = a[i + 1][:]

    return new_key, removed_ones


def move_down(a):
    n = len(a)
    new_key = [[0] * n for _ in range(len(a[0]))]
    removed_ones = sum(a[0][:])

    for i in range(1, n):
        new_key[i][:] = a[i - 1][:]
    return new_key, removed_ones


def move_left(a):
    n = len(a)
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    removed_ones = sum(a[:][len(a[0]) - 1])

    for i in range(len(a)):
        for j in range(len(a[0]) - 1):
            new_key[i][j] = a[i][j + 1]
    return new_key, removed_ones


def move_right(a):
    new_key = [[0] * len(a) for _ in range(len(a[0]))]
    removed_ones = sum(a[:][0])
    for i in range(len(a)):
        for j in range(1, len(a[0])):
            new_key[i][j] = a[i][j - 1]

    return new_key, removed_ones


def solution(key, lock):
    # count whole 0 from lock
    sum_of_zero = 0
    for i in range(len(lock)):
        for j in range(len(lock[i])):
            if lock[i][j] == 0:
                sum_of_zero += 1
    que = deque()
    answer = False
    sum_of_ones = sum(list(map(sum, tuple(map(tuple, key)))))
    key = tuple(map(tuple, key))
    que.append((key, 0, sum_of_ones))
    check = set()
    check.add(key)

    while len(que) > 0 or answer:
        kk, angle, s_of_one = que.popleft()
        if fit(kk, lock, sum_of_zero):
            # print(kk, lock)
            return True
        else:
            # up , down, right, left
            tp, rmv = move_up(kk)
            if tp.__repr__ not in check and s_of_one - rmv >= sum_of_zero:
                check.add(tp.__repr__)
                que.append((tp, angle, s_of_one - rmv))

            tp, rmv = move_down(kk)
            if tp.__repr__ not in check and sum_of_ones - rmv >= sum_of_zero:
                check.add(tp.__repr__)
                que.append((tp, angle, s_of_one - rmv))

            tp, rmv = move_right(kk)
            if tp.__repr__ not in check and sum_of_ones - rmv >= sum_of_zero:
                check.add(tp.__repr__)
                que.append((tp, angle, s_of_one - rmv))

            tp, rmv = move_left(kk)
            if tp.__repr__ not in check and sum_of_ones - rmv >= sum_of_zero:
                check.add(tp.__repr__)
                que.append((tp, angle, s_of_one - rmv))

            if angle < 270:
                tp = rotate(kk)
                if tp.__repr__ not in check :
                    check.add(tp.__repr__)
                    que.append((tp, angle + 90, s_of_one - rmv))

    return answer


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 1, 1]]))
