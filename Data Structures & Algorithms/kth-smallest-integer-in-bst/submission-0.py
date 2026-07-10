# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq

class Solution:
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                lst.append((-1 * root.val, root))
        dfs(root)
        heapq.heapify(lst)
        while len(lst) > k:
            heapq.heappop(lst)
        return -1 * heapq.heappop(lst)[0]

        