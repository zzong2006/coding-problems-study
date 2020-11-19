class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(idx):
            """
            DFS를 사용하는 방법
            """
            result = ""
            number = ""
            i = idx
            while i < len(s):
                if ord('0') <= ord(s[i]) <= ord('9'):
                    number += s[i]
                elif s[i] == '[':
                    num = int(number)
                    number = ""
                    output, idx = dfs(i + 1)
                    i = idx
                    result += (num * output)
                elif s[i] == ']':
                    return result, i
                else:
                    number = ""
                    result += s[i]

                i += 1
            return result, i

        output, _ = dfs(0)
        return output

    def stacky(self, s):
        """
        스택을 사용하는 방법
        3[a2[c]] 의 경우 예시:
            current_string = "c" 일 때의 stack은 [("", 3), ("a", 2)]
            그리고, stack.pop()은 ("a", 2) 를 불러오고, "a" + 2 * "c" 를 수행
            즉, "acc"가 완성. 다시, stack.pop()은 ("", 3)을 불러오고, "" + 3 * "acc"를 수행
            "accaccacc"가 완성
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # 숫자로 구성된 문자열을 양수 k 로 치환하는데 성공하면, 이를 스택에 넣는다.
                stack.append((current_string, k))
                # 현재 문자열을 reset 시킴
                current_string = ""
                k = 0
            elif char == "]":
                # We have completed this frame, get the last current_string and k from when the frame
                # opened, which is the k we need to duplicate the current current_string by
                last_string, last_k = stack.pop(-1)
                current_string = last_string + last_k * current_string
            elif char.isdigit():
                k = k * 10 + int(char)
            else:
                current_string += char

        return current_string

a = Solution()
# jkjk

# print(a.decodeString("2[2[y]pq4[2[jk]e1[f]]]"))
# print(a.decodeString("3[a2[c]]"))

print(a.stacky("2[2[y]pq4[2[jk]e1[f]]]"))
