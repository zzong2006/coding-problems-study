def solution(s):
    answer = 0
    max_val = 0
    for i in range(0, len(s)):
        for j in range(1, len(s) - i + 1):
            new_s = s[i : i + j]
            pal = new_s[::-1]
            if new_s == pal:
                # print(new_s)
                max_val = max(max_val, len(new_s))

    return max_val


print(solution(""))
