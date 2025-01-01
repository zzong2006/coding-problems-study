import heapq
import sys


def solution():
    get_input = sys.stdin.readline

    n = int(get_input().strip())
    board = list(map(int, get_input().strip().split()))

    hp = []
    heapq.heapify(hp)

    for i in range(n):
        heapq.heappush(hp, board[i])

    ls = [0]
    while hp:
        t = heapq.heappop(hp)
        ls.append(ls[-1] + t)
    print(sum(ls))


solution()
