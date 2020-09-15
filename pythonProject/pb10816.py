import bisect

m = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
n = int(input())
guess = list(map(int, input().split()))


def lower_bound_search(start, end, z, array):
    curr_start = start
    curr_end = end - 1
    # -10, -10, 2, 3, 3, 6, 7, 10, 10, 10
    while curr_start < curr_end:
        mid = int((curr_start + curr_end) / 2)
        if array[mid] < z:
            curr_start = mid + 1
        elif array[mid] >= z:
            curr_end = mid
    return curr_end


def upper_bound_search(start, end, z, array):
    curr_start = start
    curr_end = end - 1
    # -10, -10, 2, 3, 3, 6, 7, 10, 10, 10
    while curr_start < curr_end:
        mid = int((curr_start + curr_end) / 2)
        if array[mid] <= z:
            curr_start = mid + 1
        elif array[mid] > z:
            curr_end = mid
    return curr_end


ans = []
for i in guess:
    lb = bisect.bisect_left(arr, i)
    next_lb = bisect.bisect_right(arr, i)

    ans.append(next_lb - lb)

print(" ".join(list(map(str, ans))))
