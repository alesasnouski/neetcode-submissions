# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        i, j = head, head
        while j.next and j.next.next:
            i = i.next
            j = j.next.next

        tail_item = None
        while i:
            nxt = i.next
            i.next = tail_item
            tail_item = i
            i = nxt

        while head:
            nxt = head.next
            head.next = tail_item
            tail_item = tail_item.next
            head.next.next = nxt
            head = nxt

        

        return None
            







