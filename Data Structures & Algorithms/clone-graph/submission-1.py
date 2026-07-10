"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        old2new = {}
        def clone(old_gr):
            new_gr = Node(val = old_gr.val)
            old2new[old_gr.val] = new_gr

            for ch in old_gr.neighbors:
                if ch.val in old2new:
                    new_gr.neighbors.append(old2new[ch.val])
                else:
                    cloned = clone(ch)
                    new_gr.neighbors.append(cloned)
            return new_gr

        return clone(node)

        