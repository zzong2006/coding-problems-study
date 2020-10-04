from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def comp(time_std, param):
            h = int(time_std[:2])
            m = int(time_std[3:5])
            a_h = int(param[:2])
            a_m = int(param[3:5])
            if h > a_h:
                return False
            elif h < a_h:
                if a_h - h > 1:
                    return False
                else:  # a_h - h == 1
                    if m >= a_m:
                        return True
            else:
                return True

        answer = []
        workers = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            workers[name].append(time)
        for name in workers.keys():
            workers[name].sort()
            for i in range(len(workers[name])):
                std_time = workers[name][i]
                count = 1
                ok = False
                for j in range(i + 1, len(workers[name])):
                    if comp(std_time, workers[name][j]):
                        count += 1
                    else:
                        break
                    if count >= 3:
                        ok = True
                        answer.append(name)
                        break
                if ok:
                    break
        answer.sort()
        return answer

a = Solution()
print(a.alertNames(["daniel","daniel","daniel","luis","luis","luis","luis"],
                   ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
