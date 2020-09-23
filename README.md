# 알고리즘 문제 풀이

* [백준](https://www.acmicpc.net/)과 [프로그래머즈](https://programmers.co.kr/) 사이트에서 풀었던 문제들에 대한 코드를 올려놓은 repository입니다.
  * 코드(이하 솔루션)는 `src` 폴더에서 확인하실 수 있습니다.
    * 백준 문제에 대한 솔루션은 문제 닉네임과 문제 번호가 함께 표기되어 있습니다.
    * 프로그래머즈 문제에 대한 솔루션은 문제 닉네임만 표기되어 있습니다. 이 repository 내에서 따로 분류해야 할 것 같습니다.
    * 모든 솔루션에 대한 언어는 java 및 python 입니다.


* 다시 풀어보았으면 좋을 법한 문제들
1. [문자열 압축 (프로그래머즈)](https://programmers.co.kr/learn/courses/30/lessons/60057)
    * 굳이 String을 만들 필요 없이 개수만 계산하면 되는 것임 
    * Git Link
   
2. [숫자 카드2 (백준)](https://www.acmicpc.net/problem/10816)
    * lower_bound 또는 upper_bound 구현
    * python 으로 시도했는데 TO로 실패함. bisect library 이용해서 풀음.
    
3. [한윤정이 이탈리아에 가서 아이스크림을 사먹는데 (백준)](https://www.acmicpc.net/problem/2422)
    * 핵심은 배열을 활용하는 것 
        * 금지 조합은 2가지인데, 선택 조합은 3가지
        * 여기서는 선택 조합 보다는 금지 조합에 대한 배열을 만들고, 선택 조합을 금지 조합에 대입시켜보는 것이 맞다.
        * 예) (1,2,3) -> (1,2), (2,3), (1,3) 확인
    * python lib의 itertools combinations는 시간이 너무 오래걸림
    * 다중 for문으로 푸는것이 훨씬 빠름 (약 3배정도)

4. [경주로 건설 (프로그래머즈)](https://programmers.co.kr/learn/courses/30/lessons/67259?language=python3)
    * bfs 로 해결하는 것인데, 테스트 케이스가 부족하여서 조금 쉬운 문제가 되버림 (하지만 난 못풀었음)
    * 핵심은 dp도 적절히 섞어줘서 가지치기를 진행하는 것
    * python에서의 상하좌우 이동은 tuple로 해결하는 것이 좋다는 것을 깨달음
    * python에서의 queue는 list 보다는 collections의 deque를 사용하는 것이 좋다는 것을 깨달음

5. [자와 각도기](https://www.acmicpc.net/problem/2916)
    * queue를 이용한 bfs를 쓰면 속도가 늦다
        * 배열과 재귀를 이용한 dfs가 빠름
    * 잡설
        * 풀긴 풀었는데, 힌트를 너무 많이 봤다
        * *자*는 쓰지 않음
        * 각도의 개념을 이해하는게 중요했음
        
6. [사탕 게임](https://www.acmicpc.net/problem/3085) 
    * 구현은 어렵지 않았는데, 경우의 수가 핵심이었다. 
        * 사탕끼리 바꾼 행,열 만 고려해야되는게 아니라, 이미 바꾼 상태에서도 얻을 수 있는 최대값이 다른 어디엔가 존재한다.

7. [Maximum Sum Obtained of Any Permutation (leetcode)](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/)
    * 주어진 여러개의 구간들 중 가장 많이 중첩된 순위를 한꺼번에 계산하는법
        * 핵심 : `시작 구간`에는 `1` 그리고 `마지막 구간 + 1` 에는 `-1` 을 놓고 **굴린다**..!
        * 정말 천재적인 발상이다....
        
8. [Split a String Into the Max Number of Unique Substrings](https://leetcode.com/contest/weekly-contest-207/problems/split-a-string-into-the-max-number-of-unique-substrings/)
    * 풀긴 풀었는데 재귀로 풀었다가 TLE 나버린 case
        *   Backtracking 솔루션을 보니 훨씬 깔끔했다. 다만 이해하긴 좀 어려웠음.   
        
9. [Maximum Non Negative Product in a Matrix](https://leetcode.com/contest/weekly-contest-207/problems/maximum-non-negative-product-in-a-matrix/)
    * 두개의 dp 배열을 활용해야 하는 문제 (창의적이다)    
        * Maximum dp, Minimum dp !

10. [징검다리 건너기](https://programmers.co.kr/learn/courses/30/lessons/64062)
    * 두가지 해결 방법이 있는 문제
        * Sliding window Maximum 활용 (나는 이 방법을 썼다.. 이해하는데 오래걸렸다)
        * 이진 탐색하면서 일일이 check
         
11. [토마토](https://www.acmicpc.net/problem/7576)
    * 문제는 잘 풀었는데, python의 `deque`와 `array`의 `loop`에 관련하여 할말이 있다.
        * `for i in range(len(deque))` 가 `while len(deque) >= 1` 보다 확실하게 현재 `deque`에 포함된 모든 내용을 확인한다.
            * `while` 의 경우, `while` 문 내에서 `deque`값이 추가되면 그 값도 꺼내지게 된다. 
        * 2차원 `array`의 `loop`의 경우, 특정 값 `t`가 존재하는지 확인하고 싶다면 다음처럼 하면 좋다.
            `for i in array: if t in i: print('exist!')`
         
12. [전구와 스위치](https://www.acmicpc.net/problem/2138)
    * greedy를 이용한 해법은 간단했지만, 그걸 떠올리기에는 역부족이였음   
        * 그리고 greedy인것을 알아도 시간초과를 피하기 위해선 조금 트릭이 필요했다.
        * greedy는 경우의 수를 제한하는 방법이라는 것을 생각하자.
    * [동전 뒤집기](https://www.acmicpc.net/problem/1285)
        * 이 문제도 비슷한 문제인데, 1차원 greedy가 2차원으로 확장되었다고 생각하면 됨.
        * Combination 구할 때, bit masking을 사용하면 유용하다.
            * 예시) `for i in range(0, 1 << n):` -> 이렇게 하면 `2^n`개의 조합(yes/no)을 구할 수 있다.
        * 아무도 python으로 푼 사람이 없음, 나도 pypy3으로 채점하고 있다.
            * 그리고 greedy가 이렇게 어려운 문제인지 몰랐음;;;
        
        
13. [Majority Element II](https://leetcode.com/problems/majority-element-ii/)
    * 핵심: 크기가 `n`인 배열 중 `⌊n/2⌋` 보다 큰 값은 반드시 **한**개만 존재한다.
        * 그럼 `⌊n/3⌋` 의 경우는 ?

14. [Gas Station](https://leetcode.com/problems/gas-station/)
    * 움직이면서 자원을 충전 그리고 소모를 반복하는 문제
         * 두 가지만 파악하면 되었다.   
             1. 움직이는 사이에 문제가 없음을 확인 모든 자원 >= 소모 자원 
             2. (1)이 확인되었다면, 반드시 정답은 존재     
                -> `0~n` 방향으로 자원 충전 및 소모 진행하면서 시작 위치 찾기 
             
14. [30](https://www.acmicpc.net/problem/10610)
    * 30에 대한 배경 지식과 greedy를 이용하여 푸는 문제
    * 깨달은점
        * 어떤 수의 모든 자리의 수를 더해서 3으로 나눠지면 그 수는 3의 배수다.
        * 배수 관련 문제가 나올때는 그 배수의 값들을 나열한 뒤, 패턴을 찾아보자.
        * 입력값이 말도안되게 크면, 의외로 로직은 간단하다. 

14. [부분수열의 합](https://www.acmicpc.net/problem/14225)
    * combination을 구하는 방식이 잘못되었다.
        * 부분 수열에서 combination 구하는 것은 sliding 방식으로 구해야 한다. `(1,2,3) -> (1,2), (2,3), (1,2,3)`

15.[욕심쟁이 판다](https://www.acmicpc.net/problem/1937)
    * dfs (또는 bfs) + dp 사용 문제
        * dp 업데이트 방식이 다르다.
        * 주워 들음) dp는 한번 정하면 일반적으로 절대 수정하면 안되는 것을 원칙으로 하자.
        * 이 문제의 경우, dp의 이유 말고도, 이미 방문한 곳은 절대 방문하지 않는다.. 왜?
        
* Interval 관련 문제    
    1. [디스크 컨트롤러](https://programmers.co.kr/learn/courses/30/lessons/42627)
        * heap을 어떻게 사용하는가?
        * greedy이긴 한데 무엇을 greedy 할지 -> 방식이 잘못됬음
    2. [단속카메라](https://programmers.co.kr/learn/courses/30/lessons/42884)
        * 정확성은 옳았으나, 효율적이지 못했음
        * 이것도 greedy
    3. [회의실배정](https://www.acmicpc.net/problem/1931)
        * 핵심은 그리디 및 정렬
            * 의외로 간단한 문제였다. 하지만 난 틀렸지.
        * 열에 따른 정렬 방법 (tie 해결) `array.sort(key=lambda x: (x[1], x[0]))`
            * 두번째 열을 기준으로 오름차순 정렬 후, 두번째 열의 값이 서로 같으면 첫번째 열의 값으로 오름차순 정렬함
    
        
* 공부해야할 자료구조 또는 알고리즘
1. Segmentation Tree
    * [구간 합 구하기](https://www.acmicpc.net/problem/2042)
        * 처음 구현해봄 (트리 생성, 수정, 구간 합)
        * python3 를 사용했는데 시간초과가 자꾸 발생함 -> `sys.readline().split()` 으로 해결
            * 참고 : https://www.acmicpc.net/problem/15552
2. Trie
3. Union-Find (복습)

* python tip
    1. 재귀 함수 최대 깊이 늘리기 `sys.setrecursionlimit(10**7)` (메모리 초과 가능성 농후)
    
    