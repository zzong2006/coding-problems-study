from queue import PriorityQueue
import heapq


def solution(jobs):
    sorted(jobs, key=lambda x: x[0])
    mh = []
    removed = set()
    heapq.heapify(mh)

    answer = 0
    curr_time = 0
    saved_curr = 0
    disk_empty = True

    while len(removed) != len(jobs):
        # search
        for i in range(saved_curr, len(jobs)):
            if jobs[i][0] > curr_time:
                saved_curr = i
                break
            else:
                heapq.heappush(mh, (jobs[i][1], i))

                if i == len(jobs) - 1:
                    saved_curr = len(jobs)
        if len(mh) > 0:
            (s, idx) = heapq.heappop(mh)
            curr_time += s
            answer += (curr_time - jobs[idx][0])
            # curr_time += jobs[idx][1]
            removed.add(idx)
            print((curr_time - jobs[idx][0]), idx)
        else:
            curr_time = jobs[saved_curr][0]
    return int(answer / len(jobs))


print(solution([[0, 6], [0, 8], [7, 1]]))
