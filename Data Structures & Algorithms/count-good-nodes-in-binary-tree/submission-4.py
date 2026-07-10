# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        from copy import copy
        def good(root, levels):
            if root:
                if all([root.val >= x for x in levels]) or levels == []:
                    result.append(root.val)

                levels.append(root.val)
                lvz = copy(levels)
                good(root.left, levels)
                
                good(root.right, lvz)
        good(root, [])        
        return len(result)
        


        