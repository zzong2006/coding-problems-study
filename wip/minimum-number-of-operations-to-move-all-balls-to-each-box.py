"""
좀 더 쉽게 풀 수 있는 방법이 있는것 같아서 다시 살펴볼 필요가 있어보임.

You have n boxes. 
You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. 
Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the `i`th box.

Each answer[i] is calculated considering the initial state of the boxes.


## Example 1

Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.

## Example 2

Input: boxes = "001011"
Output: [11,8,5,4,3,4]
 
n == boxes.length
1 <= n <= 2000
boxes[i] is either '0' or '1'.

"""
from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        idx_contains_ball = [i for i, box in enumerate(boxes) if box == '1']
        answer = []
        for i in range(len(boxes)):
            answer.append(sum(abs(idx - i) for idx in idx_contains_ball))
        return answer


def test_solution():
    solution = Solution()
    assert solution.minOperations("110") == [1, 1, 3]
    assert solution.minOperations("001011") == [11, 8, 5, 4, 3, 4]
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
