# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        mem = 0
        while l1 or l2:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            sm = l1v + l2v + mem
            if sm > 9:
                tail.next = ListNode(sm-10)
                tail = tail.next
                mem = 1
            else:
                mem = 0
                tail.next = ListNode(sm)
                tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if not(l1) and not(l2) and mem !=0:
            tail.next = ListNode(mem)

        return dummy.next 
