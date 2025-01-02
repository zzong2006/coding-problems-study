"""
https://www.acmicpc.net/problem/2470

KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다.

예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 
참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.

```
5
-2 4 -99 -1 98
```

```
-99 98
```
"""
import sys


get_input = lambda: sys.stdin.readline().strip()

def solution(N: int, liquids: list[int]):
    sorted_liquids = sorted(liquids)

    left = 0
    right = N - 1
    assert len(sorted_liquids) == N
    left_right_sum = float('inf')
    answer_left = 0
    answer_right = 0

    while left < right:
        current_sum = sorted_liquids[left] + sorted_liquids[right]

        if abs(current_sum) < left_right_sum:
            left_right_sum = abs(current_sum)
            answer_left = sorted_liquids[left]
            answer_right = sorted_liquids[right]
        if current_sum == 0:
            break

        if current_sum <= 0:
            left += 1
        else:
            right -= 1

    print(f"{answer_left} {answer_right}")
    return answer_left, answer_right

def main(N=None, liquids=None):
    if N is None and liquids is None:
        N = int(get_input())
        liquids = list(map(int, get_input().split()))

    solution(N, liquids)

def test_solution():
    import numpy as np
    
    assert solution(5, [-2, 4, -99, -1, 98]) == (-99, 98)
    assert solution(2, [-1, 1]) == (-1, 1)
    assert solution(4, [-100, -2, -1, 103]) == (-100, 103)
    np.testing.assert_array_equal(solution(4, [1, 2, 3, 4]), (1, 2))
    np.testing.assert_array_equal(solution(8, [-1, -2, -3, -4, 1, 2, 3, 4]), (-4, 4))
    np.testing.assert_array_equal(solution(4, [-1, -2, -3, -4]), (-2, -1))

    print("All test cases passed")

if __name__ == "__main__":
    # test_solution()
    main()