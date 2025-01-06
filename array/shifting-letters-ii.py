"""
You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start_i, end_i, direction_i]`. 
For every `i`, shift the characters in `s` from the index `start_i` to the index `end_i` (inclusive) forward if `direction_i = 1`, or shift the characters backward if `direction_i = 0`.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). 
Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
Example 2:

Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
 
"""
import typer
from typing import List

alphabet = "abcdefghijklmnopqrstuvwxyz"
idx2alphabet = {i: alphabet[i] for i in range(len(alphabet))}
alphabet2idx = {alphabet[i]: i for i in range(len(alphabet))}

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift_list = [0] * (len(s) + 1)

        for shift in shifts:
            start, end, direction = shift
            if direction == 1:  # forward
                shift_list[start] += 1
                shift_list[end + 1] -= 1
            else:   # direction == 0, backward
                shift_list[start] -= 1
                shift_list[end + 1] += 1

        # apply shifts
        result = ""
        shift_sum = 0
        for i in range(len(s)):
            shift_sum += shift_list[i]
            shift_idx = (alphabet2idx[s[i]] + shift_sum) % len(alphabet)
            result += idx2alphabet[shift_idx]
            
        return result

def test_solution():
    for s, shifts, answer in [("abc", [[0,1,0],[1,2,1],[0,2,1]], "ace"), ("dztz", [[0,0,0],[1,1,1]], "catz")]:
        result = Solution().shiftingLetters(s, shifts)
        assert result == answer


    print("All tests passed!")

if __name__ == "__main__":
    typer.run(test_solution)
