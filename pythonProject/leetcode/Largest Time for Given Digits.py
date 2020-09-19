from collections import deque


def check(cust_time):
    hour = int(cust_time[:2])
    min = int(cust_time[2:])

    if 0 <= hour <= 23 and 0 <= min <= 59:
        return True
    else:
        return False


def convertIntToTime(strrr):
    output = ""
    strrr = str(strrr)
    if len(strrr) == 3:
        output += ("0" + strrr[:1] + ":" + strrr[1:])
    elif len(strrr) == 4:
        output += (strrr[:2] + ":" + strrr[2:])
    elif len(strrr) == 2:
        output += ("00" +":" + strrr)
    else:
        output += ("00" + ":" + "0" + strrr)
    return output

class Solution:
    def largestTimeFromDigits(self, arr) -> str:
        que = deque()
        que.append(["", [False] * 4])
        results = []

        while len(que) > 0:
            curr, visited = que.popleft()
            if len(curr) != 4:
                for i in range(len(visited)):
                    if visited[i] == False:
                        new_curr = curr
                        new_curr += str(arr[i])
                        new_visited = visited[:]
                        new_visited[i] = True
                        que.append([new_curr, new_visited])

            else:
                if check(curr):
                    results.append(int(curr))
        if len(results) <= 0 :
            return ""
        else:
            return convertIntToTime(max(results))



a = Solution()
print(a.largestTimeFromDigits([0,0,0,0]))
