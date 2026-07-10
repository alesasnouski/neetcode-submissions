# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev = head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev    

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        rev = self.reverse(head)
        x = 0
        curr, prev = rev, None
        while curr:
            if n - 1 == x:
                curr = curr.next
                if not curr:
                    return prev
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            x = x + 1

        return prev    



