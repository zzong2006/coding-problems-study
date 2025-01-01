from queue import PriorityQueue
from functools import cmp_to_key
import heapq


def least_job(curr, jbs):
    output = None
    smallest = jbs[-1]
    for i in range(0, len(jbs)):
        start, consume = jbs[i]
        if curr >= start and (
            output is None
            or output[1] > consume
            or (output[1] == consume and output[0] > start)
        ):
            output = jbs[i]
        if smallest[0] > start or (smallest[0] == start and smallest[1] > consume):
            smallest = jbs[i]
    if output is None:
        return smallest
    else:
        return output


def solution(jobs):
    curr = 0
    ls = []

    while jobs:
        found_job = least_job(curr, jobs)
        start, consume = found_job
        jobs.remove(found_job)
        # print(found_job, jobs)
        if curr < start:
            curr = start
        curr += consume
        ls.append(curr - start)
    # print(ls)
    return sum(ls) // len(ls)


print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]))
print(solution([[0, 3], [1, 9], [2, 6]]))
