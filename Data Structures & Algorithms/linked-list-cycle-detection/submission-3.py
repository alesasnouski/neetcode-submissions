# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l, r = head, head
        while True:
            if not r:
                return False
            l = l.next
            if r.next and r.next.next:
                r = r.next.next
            else:
                return False

            if l == r:
                return True    