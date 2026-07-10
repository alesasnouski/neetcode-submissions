# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import defaultdict
        levels = defaultdict(list)
        def countLevels(root, lvl):
            lvl += 1
            if root:
                levels[lvl].append(root.val)
                countLevels(root.left, lvl)
                countLevels(root.right, lvl)
        
        countLevels(root, 0)
        result = []
        for i in range(1, len(levels.values()) + 1):
            result.append(levels[i][-1])
        return result    

        