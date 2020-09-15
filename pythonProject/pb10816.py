m = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
no_overlap_arr = sorted(list(set(arr)))
n = int(input())
guess = list(map(int, input().split()))


def lower_bound_search(start, end, z, array):
    if start > end or start < 0 or end >= len(array):
        return 0
    elif start == end:
        if array[start] == z:
            return start
        else:
            return 0
    else:
        mid = int((start + end) / 2)
        if array[mid] > z:
            return lower_bound_search(start, mid - 1, z, array)
        elif array[mid] < z:
            return lower_bound_search(mid + 1, end, z, array)
        else:
            return mid


def search_left_right(index, num):
    cnt = 0
    curr = index
    while curr >= 0:
        if arr[curr] == num:
            cnt += 1
        else:
            break
        curr -= 1
    curr = index + 1
    while curr < len(arr):
        if arr[curr] == num:
            cnt += 1
        else:
            break
        curr += 1
    return cnt


ans = []
for i in guess:
    real_idx = lower_bound_search(0, m - 1, i, arr)
    if real_idx != 0:
        img_idx = lower_bound_search(0, len(no_overlap_arr) - 1, i, no_overlap_arr)
        if img_idx == len(no_overlap_arr) - 1:
            ans.append(len(arr) - real_idx)
        else:
            other_real_idx = lower_bound_search(0, m - 1, no_overlap_arr[img_idx + 1], arr)
            ans.append(other_real_idx - real_idx)
    else:
        ans.append(0)

print(" ".join(list(map(str, ans))))
