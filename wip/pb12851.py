"""
https://www.acmicpc.net/problem/12851

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

입력
첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

```
5 17
```

출력
첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

```
4
2
```
"""

import sys
import heapq

get_input = lambda: sys.stdin.readline().strip()
handle = {}
heap = []
count = 0

def solution(N: int = None, K: int = None):
    heapq.heappush(heap, (abs(N - K), (0, N)))
    min_time = abs(N - K)

    while heap:
        _, (time, position) = heapq.heappop(heap)
        if time > min_time:
            continue

        if position == K:
            if min_time == time:
                count += 1
            elif min_time > time:
                min_time = time
                count = 1
                # print(f"min_time: {min_time}, count: {count}")
            continue
        for next_position in [position - 1, position + 1, position * 2]:
            if next_position < 0 or next_position > 100000:
                # 100000을 넘으려면 *2를 해야 되는데, *2를 하기 전에 -1을 먼저 50000을 넘기 전까지 해주면 *2해서 100000 넘기고 -1하는 거보다 빠르다.
                continue

            if time + 1 <= min_time and (next_position not in handle or handle[next_position] >= time + 1):
                print(f"next_position: {next_position}, time: {time + 1}")
                handle[next_position] = time + 1
                heapq.heappush(heap, (abs(next_position - K), (time + 1, next_position)))
        # print(len(heap))

    return min_time, count

def main():
    N, K = map(int, get_input().split())
    fastest_time, count = solution(N, K)
    print(fastest_time)
    print(count)


if __name__ == "__main__":
    main()
    # test_solution()


