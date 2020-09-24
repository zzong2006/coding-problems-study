import sys
import math

get_input = sys.stdin.readline

# 0 : unknown , 1: prime , 2: not_prime
not_primes = [0] * 1000001
th = int(math.sqrt(1000001)) + 1
not_primes[0] = True
not_primes[1] = True

# 에라스토테네스의 채
for i in range(2, th):
    if not_primes[i] == 0:
        curr = i
        for k in range(2, len(not_primes) // i):
            not_primes[k * i] = True


def solution(m: int):
    done = False
    for i in range(3, m):
        if not_primes[i] == 0:
            j = m - i
            if not_primes[j] == 0 and i % 2 != 0 and j % 2 != 0:
                if i < j:
                    print("{} = {} + {}".format(m, i, j))
                    done = True
                    break
                else:
                    print("{} = {} + {}".format(m, j, i))
                    done = True
                    break
    if not done:
        print("Goldbach's conjecture is wrong.")


while True:
    n = int(get_input().strip())
    if n == 0:
        break
    else:
        solution(n)
