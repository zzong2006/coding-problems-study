import sys
import bisect

get_input = sys.stdin.readline

t = int(get_input().strip())

for i in range(t):
    n = int(get_input().strip())
    arr = list(map(int, get_input().split()))

    sorted_arr = sorted(arr)
    count = 0
    for k in range(n - 1):
        num = sorted_arr[k]
        th = 1 << (len(bin(num)) - 2)
        idx = bisect.bisect_left(sorted_arr, th, lo=k)
        # print(idx, th)
        if idx >= n:
            idx -= 1
        if sorted_arr[idx] < th:
            count += idx - k
        else:
            count += idx - k - 1

    print(count)
    # print(bisect.bisect_right(sorted_arr, 8, lo=0))
    # print(sorted_arr)
