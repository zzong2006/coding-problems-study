# 푼 문제
import sys

get_input = sys.stdin.readline

n = int(get_input().strip())

def solution(m : list):
    return sorted(m)

aa = [0] * n
for i in range(n):
    aa[i] = int(get_input().strip())

for i in solution(aa):
    print(i)
