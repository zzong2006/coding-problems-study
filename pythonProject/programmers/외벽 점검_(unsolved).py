def solution(n, weak, dist):
    def dfs(curr_weak, curr_dist, count):
        cnt = float('inf')
        if curr_weak and curr_dist:
            for i in range(len(curr_weak)):
                new_dist = curr_dist.copy()
                k = new_dist.pop()
                new_weak_clk = walk(curr_weak[i], k, curr_weak, 0)
                new_weak_anti = walk(curr_weak[i], k, curr_weak, 1)
                if len(new_weak_clk) < len(new_weak_anti):
                    cnt = min(cnt, dfs(new_weak_clk, new_dist, count + 1))
                elif len(new_weak_clk) > len(new_weak_anti):
                    cnt = min(cnt, dfs(new_weak_anti, new_dist, count + 1))
                else:
                    cnt = min(cnt, dfs(new_weak_clk, new_dist, count + 1))
                    cnt = min(cnt, dfs(new_weak_anti, new_dist, count + 1))
            return cnt
        elif not curr_weak and (not curr_dist or curr_dist):
            return count
        else:
            return float('inf')

    def walk(pos, walk_dist, curr_weaks, direction):
        """
        :param pos: 현재 위치한 장소
        :param walk_dist: 걸을 거리
        :param curr_weaks: 현재 존재하는 취약 지점
        :param direction: 0은 clock-wise, 1은 anti-clock-wise
        :return:
        """
        boundary = []
        new_weak = []
        if direction:
            if walk_dist >= n:
                boundary.append([0, n - 1])
            elif pos + walk_dist >= n:
                boundary.append([pos, n - 1])
                boundary.append([0, pos - walk_dist - n])
            else:
                boundary.append([pos, pos + walk_dist])
            for k in curr_weaks:
                for a, b in boundary:
                    if a <= k <= b:
                        break
                else:
                    new_weak.append(k)
        else:
            if walk_dist >= n:
                boundary.append([0, n - 1])
            elif pos - walk_dist < 0:
                boundary.append([0, pos])
                boundary.append([n + pos - walk_dist, n - 1])
            else:
                boundary.append([pos - walk_dist, pos])
            for k in curr_weaks:
                for a, b in boundary:
                    if a <= k <= b:
                        break
                else:
                    new_weak.append(k)
        return new_weak

    answer = 0

    dist.sort()
    for i in range(len(dist)):
        sliced_dist = dist[len(dist) - i - 1: len(dist)]
        answer = dfs(weak, sliced_dist, 0)
        if answer != float('inf'):
            return answer
    if answer == float('inf'):
        return -1
    return answer


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10]	, [3, 5, 7]))
