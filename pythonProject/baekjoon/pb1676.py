import sys


def solution():
    def get_two_and_five(number):
        two = 0
        five = 0
        while number % 2 == 0:
            two += 1
            number /= 2
        while number % 5 == 0:
            five += 1
            number /= 5
        return two, five

    get_input = sys.stdin.readline

    n = int(get_input().strip())
    two, five = 0, 0
    for i in range(1, n + 1):
        t, f = get_two_and_five(i)
        two += t
        five += f
    min_val = min(two, five)
    print(min_val)


solution()
