class Solution:
    def calculate(self, s: str) -> int:
        # remove empty space first
        new_s = ""
        for ch in s:
            if ch != "":
                new_s += ch
        s = new_s
        # calculate / , * first
        number = ""
        new_s = ""
        index = 0
        while index < len(s):
            ch = s[index]
            if ch.isdigit():
                number += ch
            else:
                left_num = None
                while index < len(s) and (ch == "*" or ch == "/"):
                    if left_num is None:
                        left_num = int(number)

                    index += 1
                    right_num = ""
                    while index < len(s):
                        inner_ch = s[index]
                        if inner_ch.isdigit():
                            right_num += s[index]
                        else:
                            break
                        index += 1
                    right_num = int(right_num)
                    if ch == "*":
                        result = left_num * right_num
                    else:
                        result = left_num // right_num
                    left_num = result
                    ch = inner_ch
                    # 연속 * 또는 / 인 경우
                if left_num is not None:
                    new_s += str(left_num)
                    number = ""
                if ch == "+" or ch == "-":
                    new_s += number
                    new_s += ch
                    number = ""
            index += 1
        if number != "":
            new_s += number

        s = new_s
        print(s)
        # calculate +, - finally
        number = ""
        new_s = ""
        index = 0
        while index < len(s):
            ch = s[index]
            if ch.isdigit():
                number += ch
            else:
                left_num = None
                while index < len(s):
                    if left_num is None:
                        left_num = int(number)

                    index += 1
                    right_num = ""
                    while index < len(s):
                        inner_ch = s[index]
                        if inner_ch.isdigit():
                            right_num += s[index]
                        else:
                            break
                        index += 1
                    right_num = int(right_num)
                    if ch == "+":
                        result = left_num + right_num
                    else:
                        result = left_num - right_num
                    left_num = result
                    ch = inner_ch
                    # 연속 + 또는 - 인 경우
                if left_num is not None:
                    new_s += str(left_num)
                    number = ""
            index += 1
        if number != "":
            new_s += number
        s = new_s
        return s


a = Solution()
print(a.calculate("3+2/4*2-7*4/2+2"))
