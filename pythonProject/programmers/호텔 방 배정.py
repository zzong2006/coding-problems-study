import sys
sys.setrecursionlimit(10 ** 7)
def solution(k, room_number):
    def find(i):
        if i not in parents:
            parents[i] = i
            return i
        else:
            k = parents[i]
            w = find(k + 1)
            parents[i] = w
            return w

    answer = []
    parents = dict()

    for i in range(len(room_number)):
        if room_number[i] not in parents:
            answer.append(room_number[i])
            parents[room_number[i]] = room_number[i]
        else:
            w = find(room_number[i])
            answer.append(w)

    return answer


print(solution(	10, [1, 3, 4, 1, 3, 1]))
