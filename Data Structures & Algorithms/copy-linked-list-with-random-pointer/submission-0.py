"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hd = head
        
        hmap = {}
        while head:
            hmap[head] = Node(head.val)
            head = head.next

        dummy = Node(0, None, None)
        start = dummy
        while hd:
            node = hmap[hd]
            node.random = hmap[hd.random] if hd.random else None
            dummy.next = node
            dummy = dummy.next
            hd = hd.next   
        
        return start.next

        