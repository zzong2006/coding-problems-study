def solution(n):
    answer = 0
    three = ""
    while n > 0:
        three += str(n % 3)
        n //= 3
    answer = int(three, 3)
    return answer


print(solution(125))
