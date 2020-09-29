# pb12969: ABC
import sys
from collections import deque



def solution():
    def backtrack(curr_string, number_of_b, number_of_c, curr_val, goal, max_length):
        if len(curr_string) == max_length:
            print(curr_string)
        if len(curr_string) == max_length and curr_val == goal:
            return curr_string
        elif len(curr_string) < max_length and curr_val <= goal:
            for alpha in ['A', 'B', 'C']:
                if alpha == 'A' and curr_val + number_of_b + number_of_c <= goal:
                    curr_string = alpha + curr_string
                    output = backtrack(curr_string, number_of_b, number_of_c, curr_val + number_of_b + number_of_c, goal, max_length)
                    if output is not None:
                        return output
                    curr_string = curr_string[1:]
                if alpha == 'B' and curr_val + number_of_c <= goal:
                    curr_string = alpha + curr_string
                    output = backtrack(curr_string, number_of_b + 1, number_of_c, curr_val + number_of_c, goal, max_length)
                    if output is not None:
                        return output
                    curr_string = curr_string[1:]
                if alpha == 'C' and curr_val <= goal:
                    curr_string = alpha + curr_string
                    output = backtrack(curr_string, number_of_b, number_of_c + 1, curr_val, goal, max_length)
                    if output is not None:
                        return output
                    curr_string = curr_string[1:]
        return None
    get_input = sys.stdin.readline
    n, k = list(map(int, get_input().strip().split()))
    answer = backtrack("", 0, 0, 0, k, n)
    print()
    if answer is None:
        print(-1)
    else:
        print(answer)
solution()