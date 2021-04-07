# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]

    # find first one
    for i in range(len(binary)):
        if binary[i] == '1':
            break

    max_length = 0
    curr = 0
    for j in range(i + 1, len(binary)):
        if binary[j] == '0':
            curr += 1
        else:
            max_length = max(max_length, curr)
            curr = 0
    max_length = max(max_length, curr)
    return max_length

solution(32)