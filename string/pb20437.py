"""
https://www.acmicpc.net/problem/20437

작년에 이어 새로운 문자열 게임이 있다. 게임의 진행 방식은 아래와 같다.

1. 알파벳 소문자로 이루어진 문자열 W가 주어진다.
2. 양의 정수 K가 주어진다.
3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.

위와 같은 방식으로 게임을 T회 진행한다.


Input
-----
문자열 게임의 수 T가 주어진다. (1 ≤ T ≤ 100)

다음 줄부터 2개의 줄 동안 문자열 W와 정수 K가 주어진다. (1 ≤ K ≤ |W| ≤ 10,000)

Example
```
2
superaquatornado
2
abcdefghijklmnopqrstuvwxyz
5
```

Output
-----
T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력한다.

만약 만족하는 연속 문자열이 없을 시 -1을 출력한다.

Example
```
4 8
-1
```
첫 번째 문자열에서 3번에서 구한 문자열은 aqua, 4번에서 구한 문자열은 raquator이다.

두 번째 문자열에서는 어떤 문자가 5개 포함된 문자열을 찾을 수 없으므로 -1을 출력한다.

"""

import sys
from collections import Counter

get_input = lambda: sys.stdin.readline().rstrip()


def solution(long_word: str, k: int):
    alpha2info = {}
    alpha_count = Counter()
    for i in range(len(long_word)):  # O(N)
        alphabet = long_word[i]
        alpha_count[alphabet] += 1
        if alphabet not in alpha2info:
            alpha2info[alphabet] = []
        alpha2info[alphabet].append(i)

    shortest_len = float("inf")
    longest_len = 0

    for alpha, count in sorted(alpha_count.items(), key=lambda x: -x[1]):
        if count < k:
            break
        # print(alpha, count, alpha2info[alpha]) # for debug
        # move as sliding window
        for i in range(len(alpha2info[alpha]) - k + 1):
            start = alpha2info[alpha][i]
            end = alpha2info[alpha][i + k - 1]
            shortest_len = min(shortest_len, end - start + 1)
            longest_len = max(longest_len, end - start + 1)

    if shortest_len == float("inf"):
        print(-1)
    else:
        print(f"{shortest_len} {longest_len}")


if __name__ == "__main__":
    t = int(get_input())
    for _ in range(t):
        long_word = get_input()
        k = int(get_input())
        solution(long_word, k)
