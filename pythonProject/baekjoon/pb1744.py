import sys


def solution():
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    arr = []
    for i in range(n):
        arr.append(int(get_input().strip()))
    arr.sort()
    # -4, -2, -1, 0, 2, 4
    # -4, -3, 3, 4, 0, 1, 3, 5, 8

    close_val_to_zero = 0
    # find the closest number to zero
    if len(arr) % 2 != 0:
        count_negative = int(arr[0] < 0)
        close_idx_to_zero = 0
        close_val_to_zero = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < 0:
                count_negative += 1

            if abs(arr[i]) < abs(close_val_to_zero):
                close_idx_to_zero = i
                close_val_to_zero = arr[i]
        if count_negative % 2 != 0:
            if close_val_to_zero == 0:
                if close_idx_to_zero == len(arr) - 1:
                    result = arr[close_idx_to_zero]
                    arr.pop(close_idx_to_zero)
                else:
                    result = arr[close_idx_to_zero + 1]
                    arr.pop(close_idx_to_zero + 1)
            elif close_val_to_zero > 0:
                result = arr[close_idx_to_zero - 1]
                arr.pop(close_idx_to_zero - 1)
            else:
                result = arr[close_idx_to_zero]
                arr.pop(close_idx_to_zero)
        elif count_negative % 2 == 0:
            if close_val_to_zero < 0:
                result = arr[close_idx_to_zero + 1]
                arr.pop(close_idx_to_zero + 1)
            else:
                result = arr[close_idx_to_zero]
                arr.pop(close_idx_to_zero)
    else:
        result = 0
    idx = 0
    while idx < len(arr):
        if (arr[idx] < 0 and arr[idx + 1] < 0) or (arr[idx] > 0 and arr[idx + 1] > 0):
            if arr[idx] * arr[idx + 1] > arr[idx] + arr[idx + 1]:
                result += arr[idx] * arr[idx + 1]
            else:
                result += arr[idx] + arr[idx + 1]
        elif (arr[idx] < 0 < arr[idx + 1]) or (arr[idx] == 0 and arr[idx + 1] > 0):
            result += arr[idx] + arr[idx + 1]
        elif arr[idx] < 0 and arr[idx + 1] == 0:
            result += arr[idx] * arr[idx + 1]
        else:
            result += arr[idx] * arr[idx + 1]
        idx += 2
    print(result)


solution()
