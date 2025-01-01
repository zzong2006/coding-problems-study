"""
https://www.acmicpc.net/problem/16395

파스칼의 삼각형은 이항계수를 삼각형 형태로 배열한 것인데, 블레즈 파스칼(1623-1662)을 따라 이름 붙여졌다.

단순한 형태로, 파스칼의 삼각형은 다음과 같은 방법으로 만들 수 있다.

N번째 행에는 N개의 수가 있다.
첫 번째 행은 1이다.
두 번째 행부터, 각 행의 양 끝의 값은 1이고, 나머지 수의 값은 바로 위 행의 인접한 두 수의 합이다.
예를 들어, n=3이면 3번째 행의 2번째 수는 위 행의 인접한 두 수 (1과 1)을 더해서 만든다.

n=6일 때, 파스칼 삼각형의 6번째 행의 10은 5번째 행의 인접한 두 수(4와 6)을 더해서 구한다.

정수 n과 k가 주어졌을 때 파스칼의 삼각형에 있는 n번째 행에서 k번째 수를 출력하는 프로그램을 작성하시오.  이때, 이 수는 이항계수 C(n-1,k-1)임에 주의하시오.

5 3 --> 6
"""

import sys
from functools import reduce

get_input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, k = map(int, get_input().split())
k = k - 1
n = n - 1

fac_cache = {}


def factorial(i):
    if i <= 1:
        return 1
    if i in fac_cache:
        return fac_cache[i]
    fac_cache[i] = i * factorial(i - 1)
    return fac_cache[i]


def nCr(n, r):
    if r == 0:
        return 1

    def _nCr(a, b):
        arr = [x for x in range(a, b)]
        if len(arr) >= 2:
            return reduce(lambda x, y: x * y, arr)
        else:
            return arr[0]

    above = _nCr(n - r + 1, n + 1)
    below = _nCr(1, r + 1)
    return above // below


if n <= 1 or k <= 0:
    print(1)
else:
    print(nCr(n - 1, k - 1) + nCr(n - 1, k))
