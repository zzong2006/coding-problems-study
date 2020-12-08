from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        matrix[0][0] = 1

        direction = 'r'
        curr = 2
        pos = [0, 0]

        change = True
        visited = set()
        while change:
            if direction in visited:
                break
            else:
                visited.add(direction)
            # move
            i, j = pos
            if direction == 'r':
                add_i = 0
                add_j = 1
            elif direction == 'l':
                add_i = 0
                add_j = -1
            elif direction == 's':
                add_i = 1
                add_j = 0
            else:  # direction == 'n':
                add_i = -1
                add_j = 0

            new_i = i + add_i
            new_j = j + add_j
            if 0 <= new_i < n and 0 <= new_j < n and matrix[new_i][new_j] == 0:
                matrix[new_i][new_j] = curr
                curr += 1
                pos = [new_i, new_j]
                visited.clear()
            else:  # change direction
                if direction == 'r':
                    direction = 's'
                elif direction == 's':
                    direction = 'l'
                elif direction == 'l':
                    direction = 'n'
                else:
                    direction = 'r'
        return matrix


a = Solution()
print(a.generateMatrix(3))
