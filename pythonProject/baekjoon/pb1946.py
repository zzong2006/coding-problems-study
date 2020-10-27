import sys
import heapq
# import matplotlib.pyplot as plt

def solution():
    get_input = sys.stdin.readline
    t = int(get_input())
    for i in range(t):
        n = int(get_input())
        people = []
        for j in range(n):
            a, b = list(map(int, get_input().strip().split()))
            people.append((a, b))
        people.sort(key=lambda x: (x[0], x[1]))
        count = 1
        # print(people)
        last = people[0][1]
        # plt.scatter(*zip(*people))
        # print(*zip(*people))
        # plt.show()
        for j in range(1, n):
            a, b = people[j]
            if last > b:
                count += 1
            last = min(last, b)
        print(count)

solution()
