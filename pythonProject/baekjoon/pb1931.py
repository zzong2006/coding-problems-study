import sys

get_input = sys.stdin.readline

intervals = []

n = list(map(int, get_input().split()))[0]

for _ in range(n):
    meeting = list(map(int, get_input().split()))
    intervals.append(meeting)
intervals.sort(key=lambda x: (x[1], x[0]))
# print(intervals)
curr = -1
count = 0
for start, end in intervals:
    if curr < 0 or start >= curr:
        curr = end
        count += 1

print(count)
# print(intervals)
