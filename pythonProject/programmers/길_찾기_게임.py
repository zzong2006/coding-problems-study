import sys
sys.setrecursionlimit(10 ** 7)

def solution(nodeinfo):
    def prefix_search(curr_pt, ls):
        if curr_pt is not None:
            ls.append(curr_pt.val)
            prefix_search(curr_pt.left, ls)
            prefix_search(curr_pt.right, ls)

    def postfix_search(curr_pt, ls):
        if curr_pt is not None:
            postfix_search(curr_pt.left, ls)
            postfix_search(curr_pt.right, ls)
            ls.append(curr_pt.val)

    new_node_info = []
    height = 0
    for i in range(len(nodeinfo)):
        x, y = nodeinfo[i]
        new_node_info.append((i + 1, x, y))
        height = max(height, y)

    new_node_info.sort(key=lambda x: (x[2], -x[1]), reverse=True)
    # binary_tree = [None] * (2 ** (height + 1))
    # root
    root = Node(*(new_node_info[0]))
    print(new_node_info)
    for i in range(1, len(new_node_info)):
        curr = root
        next_pt = root
        idx, x, y = new_node_info[i]
        while next_pt is not None and y < curr.y:
            curr = next_pt
            if curr.x > x:
                next_pt = curr.left
            else:
                next_pt = curr.right
        if curr.x > x:
            curr.left = Node(idx, x, y)
        else:
            curr.right = Node(idx, x, y)

    prefix = []
    prefix_search(root, prefix)
    # print(prefix)
    postfix = []
    postfix_search(root, postfix)
    # print(postfix)
    answer = [prefix, postfix]
    return answer


class Node:
    def __init__(self, val, x, y):
        self.val = val
        self.left = None
        self.right = None
        self.x = x
        self.y = y


print(solution([[5, 3],[11, 5]]))
