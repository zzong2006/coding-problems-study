class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check_pal(aa):
            print(aa)
            start = 0
            end = len(aa) - 1
            while start < end:
                if aa[start] != aa[end]:
                    return False
                start += 1
                end -= 1
            return True

        # a : 전위 / b : 후위
        front = 0
        back = len(a) - 1
        while front < back:
            if a[front] != b[back]:
                if front == 0:
                    if check_pal(b):
                        return True
                    if check_pal(a):
                        return True
                else:
                    if check_pal(a[:front] + b[front:]):
                        return True
                    if check_pal(a[: back + 1] + b[back + 1 :]):
                        return True
                break
            front += 1
            back -= 1
        else:
            if check_pal(a[:front] + b[front:]):
                return True

        front = 0
        back = len(a) - 1
        while front < back:
            if b[front] != a[back]:
                if front == 0:
                    if check_pal(a):
                        return True
                else:
                    if check_pal(b[:front] + a[front:]):
                        return True
                    if check_pal(b[: back + 1] + a[back + 1 :]):
                        return True
                break
            front += 1
            back -= 1
        else:
            if check_pal(b[:front] + a[front:]):
                return True

        return False


a = Solution()
print(
    a.checkPalindromeFormation(
        "aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd",
        "uvebspqckawkhbrtlqwblfwzfptanhiglaabjea",
    )
)
print(a.checkPalindromeFormation("abdef", "fecab"))
print(a.checkPalindromeFormation("x", "y"))
