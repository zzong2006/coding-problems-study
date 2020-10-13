import sys
from collections import deque, Counter


def solution():
    get_input = sys.stdin.readline
    n = list(map(int, get_input().strip().split()))[0]
    m = list(map(int, get_input().strip().split()))[0]
    board = list(map(int, get_input().strip().split()))
    cnt = Counter(board)

    board.sort()
    count = 0
    cnt[0] = 1

    for i in range(n):
        if m - board[i] > 0 and cnt[m - board[i]] > 0 and m - board[i] != board[i]:
            count += 1
            cnt[board[i]] -= 1
            cnt[m - board[i]] -= 1
    return count


print(solution())
