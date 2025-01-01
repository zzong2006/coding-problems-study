"""
https://www.acmicpc.net/problem/13144

길이가 N인 수열이 주어질 때, 수열에서 연속한 1개 이상의 수를 뽑았을 때 같은 수가 여러 번 등장하지 않는 경우의 수를 구하는 프로그램을 작성하여라.


## Input

첫 번째 줄에는 수열의 길이 N이 주어진다. (1 ≤ N ≤ 100,000)

두 번째 줄에는 수열을 나타내는 N개의 정수가 주어진다. 수열에 나타나는 수는 모두 1 이상 100,000 이하이다.

Examples (1)

```
5
1 2 3 4 5
```
15

Examples (2)

```
5
1 2 3 1 2
```

12

Examples (3)

```
5
1 1 1 1 1
```

5

"""

import sys
import math

get_input = lambda: sys.stdin.readline().rstrip()


def solution(N: int, seq: list[int]):
    pass


if __name__ == "__main__":
    N = int(get_input())
    seq = list(map(int, get_input().split()))
    print(solution(N, seq))