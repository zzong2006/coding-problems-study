import sys


def solution():
    get_input = sys.stdin.readline

    a, b, c, x, y = list(map(int, get_input().strip().split()))

    if c > (a / 2 + b / 2):
        print(x * a + y * b)
    else:
        total = 0
        if x < y:
            total += 2 * c * x
            if 2 * c < b:
                total += 2 * c * (y - x)
            else:
                total += b * (y - x)
        elif x > y:
            total += 2 * c * y
            if 2 * c < a:
                total += 2 * c * (x - y)
            else:
                total += a * (x - y)
        else:
            total += 2 * c * x
        print(total)


solution()
