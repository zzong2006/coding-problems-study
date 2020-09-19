from sys import stdin, stdout

m = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
n = int(input())
guess = list(map(int, input().split()))


def binary_search(start, end, z):
    if start > end or start < 0 or end >= len(arr):
        return 0
    elif start == end:
        if arr[start] == z:
            return 1
        else:
            return 0
    else:
        mid = int((start + end) / 2)
        if arr[mid] > z:
            return binary_search(start, mid - 1, z)
        elif arr[mid] < z:
            return binary_search(mid + 1, end, z)
        else:
            return 1


ans = []
for i in guess:
    ans.append(binary_search(0, m - 1, i))

print(" ".join(list(map(str, ans))))
