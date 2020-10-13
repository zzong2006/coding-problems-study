# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def find_middle(cc):
            m = cc
            m_d = cc
            while True:
                if m_d.next is None or m_d.next.next is None:
                    return m
                else:
                    m = m.next
                    m_d = m_d.next.next
            return m

        def _merge(l, r):
            left_start = l
            right_start = r
            print(l, r)
            if l.val < r.val:
                temp = l
                l = l.next
            else:
                temp = r
                r = r.next
            if r is None:
                temp.next = l
                return right_start
            if l is None:
                temp.next = r
                return left_start

            start_temp = temp
            while l is not None and r is not None:
                if l.val < r.val:
                    temp.next = l
                    l = l.next
                    temp = temp.next
                else:
                    temp.next = r
                    r = r.next
                    temp = temp.next
                print(start_temp)
            if l is None:
                temp.next = r
            if r is None:
                temp.next = l
            return start_temp

        def _merge_sort(curr):
            if curr.next is None:
                return curr
            else:
                print(curr)
                left = find_middle(curr)
                right = left.next
                left.next = None
                sorted_left = _merge_sort(curr)
                sorted_right = _merge_sort(right)

                print('sorted', sorted_left, sorted_right)
                sorted_link = _merge(sorted_left, sorted_right)
                return sorted_link

        head = _merge_sort(head)
        return head


a = Solution()
head = ListNode()
curr = head
for ii in [-1, 5, 3, 4, 0]:
    curr.val = ii
    curr.next = ListNode()
    curr = curr.next
print(a.sortList(head))
