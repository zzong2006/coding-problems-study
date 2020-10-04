from typing import List
import heapq


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        server = [[0, i] for i in range(k)]
        server_cnt = [0] * k

        for idx, (arr, l) in enumerate(zip(arrival, load)):
            if idx < k:
                server[idx][0] = arr + l
                server_cnt[idx] += 1
                if idx == k - 1:
                    heapq.heapify(server)
            else:
                r, sv_idx = heapq.heappop(server)
                if r <= arr:
                    heapq.heappush(server, [arr + l, sv_idx])
                    server_cnt[sv_idx] += 1
                    print(sv_idx)
            # curr = idx % k
            # if server[curr] <= arr:
            #     server[curr] = arr + l
            #     server_cnt[curr] += 1
            #     continue
            # else:
            #     curr = (curr + 1) % k
            #     while curr != (idx % k):
            #         if server[curr] <= arr:
            #             server[curr] = arr + l
            #             server_cnt[curr] += 1
            #             break
            #         else:
            #             curr = (curr + 1) % k
            #     else:
            #         continue
        m = max(server_cnt)
        answer = []
        for i in range(k):
            if server_cnt[i] == m:
                answer.append(i)
        return answer


a = Solution()
print(a.busiestServers(3, [1, 2, 3, 4, 8, 9, 10], [5, 2, 10, 3, 1, 2, 2]))
