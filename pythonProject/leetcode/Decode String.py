class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(idx):
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
        When we hit an open bracket, we know we have parsed k for the contents of the bracket, so
        push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
        the enclosed string k times.
        """
        stack = []
        current_string = ""
        k = 0

        for char in s:
            if char == "[":
                # Just finished parsing this k, save current string and k for when we pop
                stack.append((current_string, k))
                # Reset current_string and k for this new frame
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
