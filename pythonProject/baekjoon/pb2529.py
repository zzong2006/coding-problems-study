import sys
from collections import deque


def solution():
    def backtrack(idx, curr):
        if idx == len(board):
            answer[0] = min(answer[0], int("".join(list(map(str, curr)))))
            answer[1] = max(answer[1], int("".join(list(map(str, curr)))))
        else:
            for ii in range(10):
                if ii not in visited:
                    if board[idx] == "<" and curr[-1] < ii:
                        visited.add(ii)
                        backtrack(idx + 1, curr + [ii])
                        visited.remove(ii)
                    if board[idx] == ">" and curr[-1] > ii:
                        visited.add(ii)
                        backtrack(idx + 1, curr + [ii])
                        visited.remove(ii)

    def convert_to_string(a):
        nn = len(board) + 1 - len(str(a))
        if nn > 0:
            return "0" * nn + str(a)
        else:
            return str(a)

    get_input = sys.stdin.readline
    n = list(map(int, get_input().strip().split()))[0]
    board = get_input().strip().split()

    visited = set()
    answer = [sys.maxsize, -sys.maxsize]
    for i in range(10):
        visited.add(i)
        backtrack(0, [i])
        visited.remove(i)

    print(convert_to_string(answer[1]))
    print(convert_to_string(answer[0]))


solution()
