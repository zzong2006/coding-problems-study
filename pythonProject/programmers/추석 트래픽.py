import time


def solution(lines):
    def count_inner_sec(st, idx):
        count = 0
        st_first = round(st, 4)
        st_second = round(st + 1.0 - 0.001, 4)
        for w in range(len(date_times)):
            s = date_times[w]
            e = round(date_times[w] + span_times[w] - 0.001, 4)
            # print('구간 {} {}, 찾는거 {} {}'.format(st_first, st_second, s, e))
            if not (e < st_first or st_second < s):
                count += 1
        return count

    answer = 0
    date_times = []
    span_times = []
    for i in range(len(lines)):
        ts = lines[i].split(" ")
        curr_t = ts[1].split(":")
        date_times.append(
            int(curr_t[0]) * 3600 + int(curr_t[1]) * 60 + float(curr_t[2])
        )
        span_times.append(float((ts[2].split("s"))[0]))
        date_times[i] -= span_times[i]
        date_times[i] += 0.001
        date_times[i] = round(date_times[i], 4)

    start = 0
    # 시작 구간
    for k in range(len(date_times)):
        # 시작 구간
        count = count_inner_sec(date_times[k], k)
        answer = max(answer, count)
        # print(count)
        # 후방 구간
        count = count_inner_sec(date_times[k] + span_times[k] - 0.001, k)
        answer = max(answer, count)

    return answer


# print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s",
#                 "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
#                 "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s",
#                 "2016-09-15 21:00:02.066 2.62s"]))
print(solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))
print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
