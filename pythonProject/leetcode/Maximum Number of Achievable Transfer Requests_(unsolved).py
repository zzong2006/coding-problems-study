from typing import List

def recur(origin, curr, to, visit, reqs):
    search_over = True
    while search_over :
        for i in range(len(reqs)):
            [start, end] = reqs[i]
            if i not in visit:
                if end == origin and to == start and start != end:       # making circle
                    visit.add(i)
                    return True
                elif end != origin and to == start and start != end:
                    visit.add(i)
                    return recur(origin, start, end, visit, reqs)
        else:
            search_over = False
    return False

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        total = 0
        while len(requests) > 0:
            for i in range(len(requests)):
                [start, end] = requests[i]
                if start == end:
                    requests.pop(i)
                    total += 1
                    break
                visited = set()
                visited.add(i)
                if recur(start, start, end, visited, requests) :
                    for j, jk in enumerate(visited):
                        requests.pop(jk - j)
                        total += 1
                    break
                else:
                    requests.pop(i)
                    break
        return total
a = Solution()
# print(a.maximumRequests(5, [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))

print(a.maximumRequests(3,[[2,2],[2,0],[1,1],[2,1],[1,1],[2,2],[1,0],[0,2],[1,2]]))