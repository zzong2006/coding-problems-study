import sys

get_input = sys.stdin.readline


def solution(m):
    count = 0
    for changes in [500, 100, 50, 10, 5, 1]:
        count += (m // changes)
        m = m % changes

    return count



money = int(get_input().strip())
print(solution(1000 - money))