def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    else:
        n = len(s)
        for i in range(len(s) // 2 + 1):
            if s[i] != s[n - i - 1]:
                k = n - i - 1
                # remove s[i]
                new_s = s[i + 1 : k + 1]
                if new_s == new_s[::-1]:
                    return i

                # remove s[k]
                new_s = s[i:k]
                if new_s == new_s[::-1]:
                    return k

                return -1

    return -1


print(palindromeIndex("aaab"))
