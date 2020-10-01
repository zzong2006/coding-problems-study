import bisect
import sortedcontainers


class RecentCounter:

    def __init__(self):
        self.request = []
        self.start = 0
        self.end = 0

    def ping(self, t: int) -> int:
        self.request.append(t)
        s = t - 3000
        e = t
        while self.end < len(self.request):
            if self.request[self.end] <= e:
                self.end += 1
            else:
                break

        while self.start < self.end:
            if self.request[self.start] < s:
                self.start += 1
            else:
                break
        return self.end - self.start


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

l = sortedcontainers.SortedList([38, 203, 1, 45, 39, 10, 34, 90, 10, 2, 100, 1])
idx = bisect.bisect_left(l, 3)
index = l.index(39)
print(idx, l)
