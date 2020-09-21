class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = 0

        for i in text:
            if i == " ":
                count += 1

        words = text.strip().split()
        len_words = len(words)
        if len_words > 1 :
            spaces = count // (len_words - 1)
            remains = count % (len_words - 1)
        else:
            remains = count
            spaces = 0
        empty = " "
        output = ""
        for i in range(spaces):
            output += empty
        outputs = output.join(words)
        if remains == 0:
            return outputs
        elif remains >= 1:
            for i in range(remains):
                outputs += " "
            return outputs


a = Solution()
print(a.reorderSpaces("  this   is  a sentence "))
print(a.reorderSpaces(" practice   makes   perfect"))
print(a.reorderSpaces("hello   world"))
print(a.reorderSpaces("  walks  udp package   into  bar a"))
print(a.reorderSpaces("  hello"))