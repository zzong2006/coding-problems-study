import sys

def solution():
    def insert_heap(val, length):
        max_heap[length + 1] = val
        curr_idx = length + 1
        while curr_idx > 1:
            parent_idx = curr_idx // 2
            if max_heap[parent_idx] < max_heap[curr_idx]:
                max_heap[curr_idx], max_heap[parent_idx] = max_heap[parent_idx], max_heap[curr_idx]
                curr_idx = parent_idx
            else:
                break

        return length + 1

    def extract(length):
        output = max_heap[1]
        max_heap[1] = max_heap[length]
        max_heap[length] = 0
        curr_idx = 1
        # length -= 1
        while curr_idx < length:
            left = curr_idx * 2
            right = curr_idx * 2 + 1
            if left >= length:
                break
            elif left < length <= right:
                if max_heap[left] > max_heap[curr_idx]:
                    max_heap[left], max_heap[curr_idx] = max_heap[curr_idx], max_heap[left]
                    curr_idx = left
                else:
                    break
            elif right < length:
                if max_heap[left] < max_heap[right]:
                    idx = right
                else:
                    idx = left
                if max_heap[idx] > max_heap[curr_idx]:
                    max_heap[idx], max_heap[curr_idx] = max_heap[curr_idx], max_heap[idx]
                    curr_idx = idx
                else:
                    break

        return output
    get_input = sys.stdin.readline
    n = int(get_input().strip())
    max_heap = [0] * (n * 4)
    curr = 0
    for i in range(n):
        o = int(get_input().strip())
        if o == 0:
            if curr == 0:
                print(0)
            else:
                num = extract(curr)
                curr -= 1
                print(num)
                print(max_heap)
        else:
            curr = insert_heap(o, curr)
            print(max_heap)
    # print(max_heap)
solution()