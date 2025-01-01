import sys


def solution():
    get_input = sys.stdin.readline
    # 물이 새는 곳의 개수 N과 테이프의 길이 L
    n, l = list(map(int, get_input().strip().split()))
    # 물이 새는 곳의 위치는 1,000보다 작거나 같은 자연수
    board = list(map(int, get_input().strip().split()))
    board.sort()

    zum = [0] * 1001
    for b in board:
        zum[b] = 1
    count = 0
    for i in range(1, len(zum)):
        if zum[i] == 1:
            count += 1
            for j in range(i, i + l):
                if j >= len(zum):
                    return count
                zum[j] = 0
    return count


print(solution())
