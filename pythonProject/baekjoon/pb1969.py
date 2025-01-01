import sys
import heapq


def solution():
    def distance(s: str, b: str):
        z = 0
        for k in range(m):
            if s[k] != b[k]:
                z += 1
        return z

    get_input = sys.stdin.readline
    n, m = list(map(int, get_input().strip().split()))
    board = []
    answer = ""

    for i in range(n):
        st = get_input().strip()
        board.append(st)
    board.sort()

    for i in range(m):
        dna = [0] * 4
        for j in range(n):
            if board[j][i] == "T":
                dna[3] += 1
            if board[j][i] == "A":
                dna[0] += 1
            if board[j][i] == "C":
                dna[1] += 1
            if board[j][i] == "G":
                dna[2] += 1
        idx = dna.index(max(dna))
        if idx == 0:
            answer += "A"
        elif idx == 1:
            answer += "C"
        elif idx == 2:
            answer += "G"
        else:
            answer += "T"
    hap = 0
    for i in range(n):
        hap += distance(board[i], answer)
    print(answer)
    print(hap)
    return None


solution()
# print()
