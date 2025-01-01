"""
https://www.acmicpc.net/problem/2493

KOI 통신연구소는 레이저를 이용한 새로운 비밀 통신 시스템 개발을 위한 실험을 하고 있다.
실험을 위하여 일직선 위에 N개의 높이가 서로 다른 탑을 수평 직선의 왼쪽부터 오른쪽 방향으로 차례로 세우고, 각 탑의 꼭대기에 레이저 송신기를 설치하였다.
모든 탑의 레이저 송신기는 레이저 신호를 지표면과 평행하게 수평 직선의 왼쪽 방향으로 발사하고, 탑의 기둥 모두에는 레이저 신호를 수신하는 장치가 설치되어 있다.
하나의 탑에서 발사된 레이저 신호는 가장 먼저 만나는 단 하나의 탑에서만 수신이 가능하다.

예를 들어 높이가 6, 9, 5, 7, 4인 다섯 개의 탑이 수평 직선에 일렬로 서 있고, 모든 탑에서는 주어진 탑 순서의 반대 방향(왼쪽 방향)으로 동시에 레이저 신호를 발사한다고 하자.
그러면, 높이가 4인 다섯 번째 탑에서 발사한 레이저 신호는 높이가 7인 네 번째 탑이 수신을 하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신을 한다.
높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신을 하지 못한다.

탑들의 개수 N과 탑들의 높이가 주어질 때, 각각의 탑에서 발사한 레이저 신호를 어느 탑에서 수신하는지를 알아내는 프로그램을 작성하라.

첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. N은 1 이상 500,000 이하이다. 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다. 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.

Input
```
5
6 9 5 7 4
```

Output
```
0 0 2 2 4
```

stack 을 이용하여 풀어보자.
오른쪽부터 시작한 각 탑은 stack 에 넣어져서 왼쪽에 탑들과 비교하게되는데, 이때 대상(target)인 탑보다 키가 낮은 스택의 탑들은 제외된다.
그 이유는 무엇인가? 제외된 탑의 키보다 낮은 키의 탑이 대상으로 선정되면?
어차피 제외될 탑들이 수신할 수 있는 높이라면, 현재 대상인 탑 (스택에 들어갈 탑) 이 수신할 수 있는 높이가 되므로, 제외해도 상관 없다.

예를 들어, 5 7 1 2 6 일때, 6 뒤에 6 미만의 어떠한 높이의 타워가 들어와도 해당 타워가 모두 수신할 수 있으므로 1, 2 같은 타워는 모두 제외된다.

Logging 을 꼭 지워주자 시간 초과의 범인..!
"""

import sys
import logging

logging.basicConfig(level=logging.INFO)
get_input = sys.stdin.readline


def solution(n, towers):
    answers = []

    stack = []
    for i in range(n):
        while stack and towers[stack[-1]] < towers[i]:
            stack.pop()

        if stack:
            answers.append(stack[-1] + 1)
        else:
            answers.append(0)
        stack.append(i)

    print(" ".join(map(str, answers)).strip())


# echo -e "5\n6 9 5 7 4" | python3 pb2493.py
if __name__ == "__main__":
    n = int(get_input().rstrip())
    towers = list(map(int, get_input().rstrip().split()))
    solution(n, towers)
