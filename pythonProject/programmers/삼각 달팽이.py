import bisect


def solution(n):
    def curr_level(val):
        idx = bisect.bisect_left(level_curve, val)
        if level_curve[idx] >= val:
            return idx
        else:
            return idx + 1

    answer = []
    idxs = []
    total = 0
    for i in range(n):
        total += (i + 1)
    answer = [None] * total

    curr = 0
    lvl = 0
    level_curve = [1] * n
    for i in range(1, n):
        level_curve[i] = level_curve[i - 1] + (i + 1)
    print(level_curve)
    inc = curr_level(lvl + 1)
    while curr < total:

        # go down
        prev_lvl = lvl
        while 0 <= lvl < len(answer) and answer[lvl] is None:
            curr += 1
            answer[lvl] = curr
            prev_lvl = lvl
            lvl += (inc + 1)
            inc += 1
        if curr >= total:
            break

        lvl = prev_lvl
        lvl += 1
        print(answer, lvl)
        # go right
        while 0 <= lvl < len(answer) and answer[lvl] is None:
            curr += 1
            answer[lvl] = curr
            lvl += 1
        print(answer)
        if curr >= total:
            break

        lvl -= 1
        dec = curr_level(lvl + 1)
        lvl -= (dec + 1)
        dec -= 1
        # go up
        prev_lvl = lvl
        while 0 <= lvl < len(answer) and answer[lvl] is None:
            curr += 1
            answer[lvl] = curr
            prev_lvl = lvl
            lvl -= (dec + 1)
            dec -= 1
        lvl = prev_lvl
        inc = curr_level(lvl + 1)
        lvl += (inc + 1)
        inc += 1
        if curr >= total:
            break

    # a = [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
    # for idx, i in enumerate(a):
    #     idxs.append([idx, i])
    # idxs.sort(key=lambda x: x[1])
    # print(idxs)
    return answer


print(solution(5))
