# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def treeHeight(node):
            if not node:
                return [True, 0]

            hl, hr = treeHeight(node.left), treeHeight(node.right)
            balanced = hl[0] and hr[0] and abs(hl[1] - hr[1]) <= 1
            return [balanced, 1 + max(hl[1], hr[1])]
        
        return treeHeight(root)[0]